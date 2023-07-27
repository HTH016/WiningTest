# from django.shortcuts import render
from django.views.generic.base import View

# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http.response import HttpResponse
from detail.models import WinWine, WinWineRegion, WinDetailView, WinDetailViewN
from _datetime import datetime
from django.utils.dateformat import DateFormat


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_client_ip_psuedo(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


class WineDetailInfoView(View):
    def get(self, request):
        template = loader.get_template("detail/wineDetail.html")
        wine_id = request.GET["wine_id"]
        wine_info = WinWine.objects.get(wine_id=wine_id)
        region = WinWineRegion.objects.get(wine_region_id=wine_info.wine_region_id)

        if request.session.get("memid"):
            detail_rec = WinDetailView(
                user_id=request.session.get("memid"),
                wine_id=wine_id,
                detail_view_time=DateFormat(datetime.now()).format("Y-m-d h:i:s"),
            )
            detail_rec.save()

        else:
            detail_n_rec = WinDetailViewN(
                wine_id=wine_id,
                detail_view_n_time=DateFormat(datetime.now()).format("Y-m-d h:i:s"),
            )
            detail_n_rec.save()
        # 사용자 상세 보기 기록 남기기
        context = {
            "wine_info": wine_info,
            "region": region,
        }
        return HttpResponse(template.render(context, request))
