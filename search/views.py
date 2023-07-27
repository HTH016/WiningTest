from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http.response import HttpResponse
from detail.models import WinWine
from django.db.models import Q
import difflib
from search.models import WinSearch, WinSearchN
from _datetime import datetime
from django.utils.dateformat import DateFormat
from user.models import WinUser, WinUserFavorite
from search.functions.functions import (
    win_corr_code,
    win_corr_cap,
    win_corr_alc,
    win_reco_alc,
    win_reco_color,
    win_reco_food,
    win_reco_taste,
    win_corr_alc_inverse,
    sort,
)


# Create your views here.


# class SearchMainView( View ):
#     @method_decorator( csrf_exempt )
#     def dispatch(self, request, *args, **kwargs):
#         return View.dispatch(self, request, *args, **kwargs)
#     def get(self, request ):
#         template = loader.get_template( "search/main.html" )
#         context = {}
#         return HttpResponse( template.render( context, request ) )
#


class SearchByNameView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("search/main.html")
        context = {}
        return HttpResponse(template.render(context, request))  # 검색 페이지

    def post(self, request):
        search_word = request.POST.get("searchname")  # 검색어를 받는다.
        template = loader.get_template("search/searchByNameList.html")
        dtos_results = WinWine.objects.filter(
            wine_name__contains=search_word
        )  # 입력 문자열이 이름에 포함된 것
        results_count = dtos_results.count()

        if request.session.get("memid"):
            search_rec = WinSearch(
                user_id=request.session.get("memid"),
                search_word=search_word,
                search_time=DateFormat(datetime.now()).format("Y-m-d h:i:s"),
            )
            search_rec.save()

        else:
            search_n_rec = WinSearchN(
                search_n_word=search_word,
                search_n_time=DateFormat(datetime.now()).format("Y-m-d h:i:s"),
            )
            search_n_rec.save()

        context = {
            "dtos_results": dtos_results,
            "results_count": results_count,
        }

        return HttpResponse(template.render(context, request))


class SearchByCategoryView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("search/searchByCategory.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("search/searchByCategoryList.html")
        list_kind = list(map(int, request.POST.getlist("winekind")))
        list_capacity = list(map(int, request.POST.getlist("winecapacity")))
        list_alcohol = list(map(int, request.POST.getlist("winealcohol")))
        list_dangdo = list(map(int, request.POST.getlist("dangdo")))
        list_sando = list(map(int, request.POST.getlist("sando")))
        list_tannin = list(map(int, request.POST.getlist("tannin")))
        list_food = list(map(int, request.POST.getlist("winefood")))
        list_region = list(map(int, request.POST.getlist("wineregion")))

        # getlist 로 dropbox 의 여러 값을 리스트로 받는다.
        # 리스트 성분들을 전부 문자열로 받아서 숫자로 변환해야한다. map(함수, 리스트) 로 리스트 성분에 함수를 적용한다.
        # 함수를 적용한 성분들을 다시 성분으로 하는 리스트를 얻는다.

        dtos_results = WinWine.objects.all().filter(
            wine_sort__in=list(map(win_corr_code, list_kind)),
            wine_capacity__in=list(map(win_corr_cap, list_capacity)),
            # wine_alcohol__in = list( float, list( map( win_corr_alc, list_alcohol ) ) ),
            wine_dangdo__in=list(map(win_corr_code, list_dangdo)),
            wine_sando__in=list(map(win_corr_code, list_sando)),
            wine_tannin__in=list(map(win_corr_code, list_tannin)),
            wine_food__in=list(map(win_corr_code, list_food)),
            wine_region__in=list(map(win_corr_code, list_region)),
        )

        results_count = dtos_results.count()

        context = {
            "list_kind": list(map(win_corr_code, list_kind)),
            "list_capacity": list(map(win_corr_cap, list_capacity)),
            "list_dangdo": list(map(win_corr_code, list_dangdo)),
            "list_sando": list(map(win_corr_code, list_sando)),
            "list_tannin": list(map(win_corr_code, list_tannin)),
            "list_food": list(map(win_corr_code, list_food)),
            "list_region": list(map(win_corr_code, list_region)),
            "dtos_results": dtos_results,
            "results_count": results_count,
        }

        return HttpResponse(template.render(context, request))


class SearchByUserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("search/searchByUser.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        user_id = request.session.get("memid")
        user = WinUser.objects.get(user_id=user_id)
        print(user_id)
        print(user)

        fav_dto = WinUserFavorite.objects.get(user_id=user.user_id)
        user_favorite = [
            fav_dto.fav_wine_color,
            fav_dto.fav_alc,
            fav_dto.fav_sweet,
            fav_dto.fav_bitter,
            fav_dto.fav_sour,
            fav_dto.fav_food,
        ]
        print(user_favorite)
        arr = [0.05]
        user_prior = arr * 6
        user_prior[fav_dto.fav_first_priority - 1] += 0.45
        user_prior[fav_dto.fav_second_priority - 1] += 0.20
        user_prior[fav_dto.fav_third_priority - 1] += 0.05
        print(user_prior)
        wine_rearrange = []
        dto_list = []

        wine_dtos = WinWine.objects.only(
            "wine_id",
            "wine_name",
            "wine_image",
            "wine_sort",
            "wine_alc",
            "wine_dangdo",
            "wine_sando",
            "wine_tannin",
            "wine_food",
        ).order_by("wine_id")
        results_count = wine_dtos.count()
        print(results_count)

        for wine_dto in wine_dtos:
            color_score = win_reco_color(user_favorite[0], wine_dto.wine_sort)
            alc_score = win_reco_alc(
                user_favorite[1], win_corr_alc_inverse(wine_dto.wine_alc)
            )
            sweet_score = win_reco_taste(user_favorite[2], wine_dto.wine_dangdo)
            bitter_score = win_reco_taste(user_favorite[3], wine_dto.wine_tannin)
            sour_score = win_reco_taste(user_favorite[4], wine_dto.wine_sando)
            food_score = win_reco_food(user_favorite[5], wine_dto.wine_food)

            user_similarity = (
                color_score * user_prior[0]
                + alc_score * user_prior[1]
                + sweet_score * user_prior[2]
                + bitter_score * user_prior[3]
                + sour_score * user_prior[4]
                + food_score * user_prior[5]
            )
            # print([color_score, alc_score, sweet_score, bitter_score, sour_score, food_score])
            # print([user_prior[0], user_prior[1], user_prior[2], user_prior[3], user_prior[4], user_prior[5]])
            # print(user_similarity)
            wine_rearrange.append(user_similarity)
            dto_list.append(wine_dto.wine_id)

        # print( len(wine_rearrange))
        print(dto_list)
        print(wine_rearrange)
        search_rearrange = sort(wine_rearrange, dto_list)

        print(search_rearrange)

        template = loader.get_template("search/searchByUserList.html")
        context = {"results_count": results_count}
        return HttpResponse(template.render(context, request))


class SearchByRankView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return View.dispatch(self, request, *args, **kwargs)

    def get(self, request):
        template = loader.get_template("search/searchByRank.html")
        context = {}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template("search/searchByRankList.html")

        rank_category = request.POST.get("rank_category")
        rank_qnty = request.POST.get("rank_qnty")

        # # 조회수
        # if rank_category == detailview :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)
        #
        # # 구매수
        # elif rank_category == purchaseqnty :
        #     list_by_rank =  WinWine.objects
        #     .prefetch_related("wine_id")
        #     .prefetch_related("sell_id").filter(user_id=user_id)
        #     .prefetch_related("storeUrl")
        #     .values
        #
        # # 판매 등록 수
        # elif rank_category == sellregist :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)
        #
        # # 리뷰 개수
        # elif rank_category == reviewqnty :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)
        #
        # # 리뷰 평점
        # elif rank_category == reviewavg :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)
        #
        # # 게시판 언급
        # elif rank_category == boardword :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)
        #
        # # 평균 가격
        # elif rank_category == priceavg :
        #     list_by_rank = WinWine.objects.filter(wine_name__contains=search_word)

        context = {}
        return HttpResponse(template.render(context, request))

    # 조회수            win_detail_view, win_detail_view_n

    # 구매수            win_sell, win_purchase_detail
    # 판매 등록 수        win_sell
    # 리뷰 개수            win_sell, win_review
    # 리뷰 평점            win_sell, win_review
    # 게시판 언급            win_board
    # 평균 가격             win_purchase_detail, win_sell
