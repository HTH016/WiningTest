from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.template import loader
from django.http.response import HttpResponse, JsonResponse
from store.models import WinStore, WinSell
from detail.models import WinWine
from django.utils.dateformat import DateFormat
from datetime import datetime
from store.db_access.query_set import (
    insert_store_info,
    insert_sell_info,
    delete_store_info,
    check_store_product_info,
    check_store_regist_number,
    get_store_info,
    get_detail_sell_list,
    get_product_list_by_seller,
    delete_product,
    check_passwd,
    drop_store_info,
    get_store_revenue,
)
from django.db.utils import DatabaseError
import json

# Create your views here.

# 일반 정보 입력 후 매장 정보 등록
# user 회원가입에서 넘어온다.
# temp_id 는 회원가입 시 입력한 id이고, 점주 회원가입이 모두 끝날 때 까지 전달, 보존하고 파기한다.
# temp_id 를 GET이 아닌 session으로부터 받는다.


class StoreRegistrationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        user_id = request.session.get("temp_id")
        print(user_id)
        print(check_store_product_info(user_id=user_id))

        if check_store_product_info(user_id=user_id):
            return redirect("storeMyPage")

        else:
            template = loader.get_template("store/storeRegistration.html")
            context = {"user_id": user_id}
            return HttpResponse(template.render(context, request))

    # storeRegistration.html
    # storeRegistrationScript.js 를 import 한다.
    # storeRegistrationScript.js에서 입력값에 대한 유효성 검사, 위치 url API 를 import 했다.

    def post(self, request):
        user_id = request.POST.get("userId", None)
        main_address = request.POST.get("mainAddress", None)
        detail_address = request.POST.get("detailAddress", None)
        store_name = request.POST.get("storeName", None)
        store_reg_num = request.POST.get("storeRegNum", None)
        store_email = request.POST.get("storeEmail")
        store_map_url = request.POST.get("storeMapUrl", None)

        store_address = main_address + "@" + detail_address
        # 파이썬에서도 정규식 검증하고 db insert하기

        try:
            insert_store_info(
                user_id=user_id,
                store_address=store_address,
                store_name=store_name,
                store_reg_num=store_reg_num,
                store_email=store_email,
                store_map_url=store_map_url,
            )

        except DatabaseError:
            redirect("errorhandling:storeError")

        return redirect("productAddition")

    # insert_store_info 라는 함수를 정의하여 사용했다.


class CheckStoreRegistNumberView(View):
    def get(self, request):
        reg_num = request.GET.get("regnum", None)

        if reg_num == None:
            return JsonResponse({"result": "문제가 발생했습니다 잠시 후 다시 시도해주세요"}, status=200)

        else:
            result = check_store_regist_number(reg_num=reg_num)

            if result == True:
                return JsonResponse(
                    {"result": "유효한 사업자 등록번호입니다", "code": "1"}, status=200
                )

            else:
                return JsonResponse(
                    {"result": "이미 등록된 사업자 등록번호입니다", "code": "-1"}, status=200
                )

    # js/productAdditionScript.js 를 import
    #


class ProductAdditionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        user_id = request.session.get("temp_id")
        modify = request.GET.get("mdfy", None)
        print(modify)
        wines = WinWine.objects.values(
            "wine_id", "wine_name", "wine_capacity", "wine_alc"
        )
        product_list = get_product_list_by_seller(user_id=user_id)
        store_id = WinStore.objects.get(user_id=user_id).store_id

        template = loader.get_template("store/productAddition.html")
        context = {
            "wines": wines,
            "store_id": store_id,
            "product_list": product_list,
            "modify": modify,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        user_id = request.session.get("temp_id")
        store_id = request.POST.get("storeId", None)
        sell_ids = request.POST.getlist("sellId", None)
        wine_ids = request.POST.getlist("wineId", None)
        sell_prices = request.POST.getlist("sellPrice", None)
        sell_promots = request.POST.getlist("sellPromot", None)
        sell_state = 1
        btn_cancel_regist = request.POST.get("btnCancelRegist", None)
        btn_product_add = request.POST.get("btnProductAdd", None)
        btn_back = request.POST.get("btnBackRegist", None)
        current_time = DateFormat(datetime.now()).format("Y-m-d H:i:s")

        if btn_product_add != None:
            print("product add")
            try:
                insert_sell_info(
                    user_id,
                    store_id,
                    wine_ids,
                    current_time,
                    sell_ids,
                    sell_prices,
                    sell_promots,
                    sell_state,
                )
                if len(sell_ids) != 0:
                    return redirect("productList")
                else:
                    return redirect("storeMyPage")
            except DatabaseError:
                return redirect("errorhandling:storeError")

        elif btn_cancel_regist != None:
            delete_store_info(store_id=store_id)
            return redirect("storeRegistration")  # user mypage로 리다이렉트 해야함

        elif btn_back != None:
            delete_store_info(store_id=store_id)
            return redirect("storeRegistration")


class SearchProduct(View):
    def get(self, request):
        search_keyword = request.GET.get("srhkeyword", None)

        result_obj1 = WinWine.objects.filter(
            wine_name__icontains=search_keyword, wine_name__range=("가", "힣")
        ).values_list("wine_id", "wine_name", "wine_capacity", "wine_alc")
        # print(result_obj1[0][0], result_obj1[0][1], result_obj1[0][2], result_obj1[0][3])
        #
        #
        # print(result_obj1[0])

        result = []
        if result_obj1 == None:
            result = "no result"

        else:
            for i in range(len(result_obj1)):
                result.append(result_obj1[i])

        # result_obj2 = list(result_obj1.wine_id)
        # print(result_obj2)
        # result_obj3 = list(result_obj1.wine_name)
        # print(result_obj3)
        # result_obj4 = list(result_obj1.wine_alc)
        # print(result_obj4)
        # start = time()
        #
        # result = WinWine.objects.filter(wine_name_eng__iconteaints = search_keyword)
        #
        # end = time()
        #
        # print(end - start)

        # return JsonResponse({"result":result}, status = 200)
        return JsonResponse({"result": result}, status=200)


class DiscontinueProductView(View):
    def get(self, request):
        user_id = "test4444"
        wine_id = request.GET.get("wineid", None)
        print(wine_id)
        delete_product(wine_id=wine_id, user_id=user_id)

        return JsonResponse({"result": "삭제되었습니다"}, status=200)


class StoreMyPageView(View):
    def get(self, request):
        user_id = request.session.get("memid")
        template = loader.get_template("store/storeMyPage.html")
        context = {"user_id": user_id}

        return HttpResponse(template.render(context, request))


class SearchReceiveCodeView(View):
    def get(self, request):
        template = loader.get_template("store/searchReceiveCode.html")
        user_id = request.session.get("memid")

        context = {}
        return HttpResponse(template.render(context, request))

    # 수령코드 get 방식으로 검색할지 post 방식으로 검색할지 결정하기


class StoreInfoView(View):
    def get(self, request):
        template = loader.get_template("store/storeInfo.html")
        user_id = request.session.get("memid")
        info = get_store_info(user_id=user_id)[0]
        full_address = info.get("store_address").split("@")
        main_address = full_address[0]
        detail_address = full_address[1]

        context = {
            "info": info,
            "main_address": main_address,
            "detail_address": detail_address,
        }
        return HttpResponse(template.render(context, request))

        # get_store_info : user_id 가 같은 모든 row를 select한다. 가장 최근의 row를 선택하기 위해 [0]을 붙인다.
        # split 은 주어진 문자열을 기준으로 list로 나눈다.


class StoreInfoModificationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("store/storeInfoModification.html")
        user_id = request.session.get("memid")
        info = get_store_info(user_id=user_id)[0]
        full_address = info.get("store_address").split("@")
        main_address = full_address[0]
        detail_address = full_address[1]

        context = {
            "info": info,
            "main_address": main_address,
            "detail_address": detail_address,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        user_id = request.session.get("memid")
        main_address = request.POST.get("mainAddress", None)
        detail_address = request.POST.get("detailAddress", None)
        store_name = request.POST.get("storeName", None)
        store_reg_num = request.POST.get("storeRegNum", None)
        store_email = request.POST.get("storeEmail")
        store_map_url = request.POST.get("storeMapUrl", None)

        store_address = main_address + "@" + detail_address
        # 파이썬에서도 정규식 검증하고 db insert하기

        try:
            insert_store_info(
                user_id=user_id,
                store_address=store_address,
                store_name=store_name,
                store_reg_num=store_reg_num,
                store_email=store_email,
                store_map_url=store_map_url,
            )

        except DatabaseError:
            redirect("errorhandling:storeError")

        return redirect("storeInfo")


class SellListView(View):
    def get(self, request):
        user_id = request.session.get("memid")
        page_num = request.GET.get("pageNum", 1)
        template = loader.get_template("store/sellList.html")
        list_count = 30
        end = int(list_count) * int(page_num)
        start = end - 29
        # list_info =


class SellDetailListView(View):
    def get(self, request):
        user_id = request.session.get("memid")
        page_num = request.GET.get("pageNum", 1)
        template = loader.get_template("store/sellDetailList.html")
        list_count = 30
        end = int(list_count) * int(page_num)
        start = end - 29
        list_info = get_detail_sell_list(user_id=user_id, start=start, end=end)
        # detail_sell_list()
        list_length = list_info[0]
        detail_sell_list = list_info[1]
        pages = (list_length // list_count) + 1

        pages = [i + 1 for i in range(pages)]

        context = {"list": detail_sell_list, "pages": pages}
        return HttpResponse(template.render(context, request))


class ProductListView(View):
    def get(self, request):
        template = loader.get_template("store/productList.html")
        user_id = request.session.get("memid")
        product_list = get_product_list_by_seller(user_id=user_id)

        context = {"product_list": product_list}

        return HttpResponse(template.render(context, request))


class DropStoreView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("store/dropStore.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        passwd = json.loads(request.body).get("passwd", None)
        user_id = request.session.get("memid")
        result = check_passwd(user_id=user_id, passwd=passwd)

        if result == 0:
            text = "비밀번호가 다릅니다"
            code = -1

        elif result == 1:
            try:
                drop_store_info(user_id=user_id)
                text = "등록된 점포가 삭제 되었습니다"
                code = 1
            except Exception as ex:
                text = "문제가 발생했습니다 잠시 후 다시 시도해주세요"
                code = -1
                print(ex)
                return JsonResponse({"result": text, "code": code}, status=200)
        return JsonResponse({"result": text, "code": code}, status=200)


class StoreRevenueMainView(View):
    def get(self, request):
        user_id = request.session.get("memid")
        template = loader.get_template("store/storeRevenueMain.html")
        revenue_info = get_store_revenue(user_id=user_id)

        context = {"revenue_info": revenue_info}
        return HttpResponse(template.render(context, request))


class StoreRevenueTermView(View):
    def get(self, request):
        user_id = request.session.get("memid")
        term = int(request.GET.get("term", 0))
        print(term)
        revenue_info = get_store_revenue(user_id=user_id, term=term)
        print(revenue_info)
        return JsonResponse({"result": revenue_info}, status=200)
