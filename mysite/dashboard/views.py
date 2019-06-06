from django.shortcuts import render
from .models import *

from django.http import Http404, JsonResponse
# Create your views here.

def dashboard1(request):
    return render(request, 'landing/index1.html')

def dash(request):
    return render(request, 'dash/dash.html')

def table(request):
    return render(request, 'table/table.html')

def test(request):
    return render(request, 'test/test.html')

def dashboardgr(request):
    return render(request, 'dashboard/dashboard.html')
def dashboardgrimages(request):
    return render(request, 'dashboard/dashboardimages.html')


def fridge(request):
    return render(request, 'graphs/Fridge.html')

def redshelf(request):
    return render(request, 'graphs/RedShelf.html')

def panorama(request):
    return render(request, 'graphs/Panorama.html')

def glassfridge(request):
    return render(request, 'graphs/GlassFridge.html')


def glassfridgeimages(request):
    return render(request, 'graphsImages/GlassFridge.html')



def philipmorris(request):
    return render(request, 'graphs/PhilipMorris.html')










def display_data(request):
    div_arr = []
    items = ColaFridge.objects.all()


    for item in items:
        if item.label == "cap":
            div_arr.append(float(item.diagonals))
    div_arr = sorted(div_arr, reverse=True)
    context = {
    'div_arr': div_arr,
        'items': items,

    }

    return render(request, 'table/table.html', context)

def add_ajax(request):
    if request.is_ajax():
        items = ColaFridge.objects.all()
        #len_d = []
#diagonals
        div_arr = []
        div_arr_cap_fan = []
        div_arr_cap_spr = []

        div_arr_l = []
        div_arr_l_fan = []
        div_arr_l_spr = []

        div_arr_b = []
        div_arr_b_fan = []
        div_arr_b_spr = []
#sides
        s_arr = []
        s_arr_cap_fan = []
        s_arr_cap_spr = []

        s_arr_l = []
        s_arr_l_fan = []
        s_arr_l_spr = []

        s_arr_b = []
        s_arr_b_fan = []
        s_arr_b_spr = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr.append(float(item.diagonals))
                s_arr.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "cap_fanta":
                div_arr_cap_fan.append(float(item.diagonals))
                s_arr_cap_fan.append(float(item.sides))

            if item.label == "cap_sprite":
                div_arr_cap_spr.append(float(item.diagonals))
                s_arr_cap_spr.append(float(item.sides))

            if item.label == "label_fanta":
                div_arr_l_fan.append(float(item.diagonals))
                s_arr_l_fan.append(float(item.sides))

            if item.label == "label_sprite":
                div_arr_l_spr.append(float(item.diagonals))
                s_arr_l_spr.append(float(item.sides))

            if item.label == "bottle0.5L":
                div_arr_b.append(float(item.diagonals))
                s_arr_b.append(float(item.sides))

            if item.label == "bottle0.5L_fanta":
                div_arr_b_fan.append(float(item.diagonals))
                s_arr_b_fan.append(float(item.sides))

            if item.label == "bottle0.5L_sprite":
                div_arr_b_spr.append(float(item.diagonals))
                s_arr_b_spr.append(float(item.sides))

        div_arr = sorted(div_arr, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_cap_fan = sorted(div_arr_cap_fan, reverse=True)
        div_arr_cap_spr = sorted(div_arr_cap_spr, reverse=True)
        div_arr_l_fan = sorted(div_arr_l_fan, reverse=True)
        div_arr_l_spr = sorted(div_arr_l_spr, reverse=True)
        div_arr_b = sorted(div_arr_b, reverse=True)
        div_arr_b_fan = sorted(div_arr_b_fan, reverse=True)
        div_arr_b_spr = sorted(div_arr_b_spr, reverse=True)

        s_arr = sorted(s_arr, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_cap_fan = sorted(s_arr_cap_fan, reverse=True)
        s_arr_cap_spr = sorted(s_arr_cap_spr, reverse=True)
        s_arr_l_fan = sorted(s_arr_l_fan, reverse=True)
        s_arr_l_spr = sorted(s_arr_l_spr, reverse=True)
        s_arr_b = sorted(s_arr_b, reverse=True)
        s_arr_b_fan = sorted(s_arr_b_fan, reverse=True)
        s_arr_b_spr = sorted(s_arr_b_spr, reverse=True)


        len_cap = []
        len_cap_fan = []
        len_cap_spr = []
        len_l  = []
        len_l_fan = []
        len_l_spr = []
        len_b = []
        len_b_fan = []
        len_b_spr = []


        for i in range(1,len(div_arr)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_cap_fan)):
            len_cap_fan.append(i)
        for i in range(1,len(div_arr_cap_spr)):
            len_cap_spr.append(i)
        for i in range(1,len(div_arr_l_fan)):
            len_l_fan.append(i)
        for i in range(1,len(div_arr_l_spr)):
            len_l_spr.append(i)
        for i in range(1,len(div_arr_b)):
            len_b.append(i)
        for i in range(1,len(div_arr_b_fan)):
            len_b_fan.append(i)
        for i in range(1,len(div_arr_b_spr)):
            len_b_spr.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_cap_fan[-1]
        d = len_cap_spr[-1]
        e = len_l_fan[-1]
        j = len_l_spr[-1]
        z = len_b[-1]
        u = len_b_fan[-1]
        i = len_b_spr[-1]


        co_data = [a,b,c,d,e,j,z,u,i]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'div_arr': div_arr,
                'len_d': len_cap,
                'div_arr_l': div_arr_l,
                'div_arr_cap_fan': div_arr_cap_fan,
                'div_arr_cap_spr': div_arr_cap_spr,
                'div_arr_l_fan': div_arr_l_fan,
                'div_arr_l_spr': div_arr_l_spr,
                'div_arr_b ': div_arr_b,
                'div_arr_b_fan': div_arr_b_fan,
                'div_arr_b_spr': div_arr_b_spr,

                's_arr': s_arr,
                's_arr_l': s_arr_l,
                's_arr_cap_fan': s_arr_cap_fan,
                's_arr_cap_spr':s_arr_cap_spr,
                's_arr_l_fan':s_arr_l_fan,
                's_arr_l_spr': s_arr_l_spr,
                's_arr_b ': s_arr_b,
                's_arr_b_fan': s_arr_b_fan,
                's_arr_b_spr': s_arr_b_spr,



            }
        return JsonResponse(response)
    else:
        raise Http404



def add_ajaxtwo(request):
    if request.is_ajax():
        items = ColaRedShelf.objects.all()
        #len_d = []
#diagonals
        div_arr_cap = []
        div_arr_l = []
        div_arr_b_one = []
        div_arr_b_pol = []
        div_arr_b_two = []
#sides
        s_arr_cap = []
        s_arr_l = []
        s_arr_b_one = []
        s_arr_b_pol = []
        s_arr_b_two = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr_cap.append(float(item.diagonals))
                s_arr_cap.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "bottle1L":
                div_arr_b_one.append(float(item.diagonals))
                s_arr_b_one.append(float(item.sides))

            if item.label == "bottle1.5L":
                div_arr_b_pol.append(float(item.diagonals))
                s_arr_b_pol.append(float(item.sides))

            if item.label == "bottle2L":
                div_arr_b_two.append(float(item.diagonals))
                s_arr_b_two.append(float(item.sides))


        div_arr_cap = sorted(div_arr_cap, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_b_one = sorted(div_arr_b_one, reverse=True)
        div_arr_b_pol = sorted(div_arr_b_pol, reverse=True)
        div_arr_b_two = sorted(div_arr_b_two, reverse=True)


        s_arr_cap = sorted(s_arr_cap, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_b_one = sorted(s_arr_b_one, reverse=True)
        s_arr_b_pol = sorted(s_arr_b_pol, reverse=True)
        s_arr_b_two = sorted(s_arr_b_two, reverse=True)


        len_cap = []
        len_l = []
        len_b_one = []
        len_b_pol  = []
        len_b_two = []



        for i in range(1,len(div_arr_cap)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_b_one)):
            len_b_one.append(i)
        for i in range(1,len(div_arr_b_pol)):
            len_b_pol.append(i)
        for i in range(1,len(div_arr_b_two)):
            len_b_two.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_b_one[-1]
        d = len_b_pol[-1]
        e = len_b_two[-1]



        co_data = [a,b,c,d,e]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'len_d': len_cap,

                'div_arr_cap': div_arr_cap,
                'div_arr_l': div_arr_l,
                'div_arr_b_one': div_arr_b_one,
                'div_arr_b_pol': div_arr_b_pol,
                'div_arr_b_two': div_arr_b_two,

                's_arr_cap': s_arr_cap,
                's_arr_l': s_arr_l,
                's_arr_b_one': s_arr_b_one,
                's_arr_b_pol':s_arr_b_pol,
                's_arr_b_two':s_arr_b_two,


            }
        return JsonResponse(response)
    else:
        raise Http404



def add_ajaxthree(request):
    if request.is_ajax():
        items = Panorama.objects.all()
        #len_d = []
#diagonals
        div_arr_cap = []
        div_arr_l = []
        div_arr_b_one = []
        div_arr_b_pol = []
        div_arr_b_two = []
#sides
        s_arr_cap = []
        s_arr_l = []
        s_arr_b_one = []
        s_arr_b_pol = []
        s_arr_b_two = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr_cap.append(float(item.diagonals))
                s_arr_cap.append(float(item.sides))
            if item.label == "label":
                div_arr_l.append(float(item.diagonals))
                s_arr_l.append(float(item.sides))

            if item.label == "bottle1L":
                div_arr_b_one.append(float(item.diagonals))
                s_arr_b_one.append(float(item.sides))

            if item.label == "bottle1.5L":
                div_arr_b_pol.append(float(item.diagonals))
                s_arr_b_pol.append(float(item.sides))

            if item.label == "bottle2L":
                div_arr_b_two.append(float(item.diagonals))
                s_arr_b_two.append(float(item.sides))


        div_arr_cap = sorted(div_arr_cap, reverse=True)
        div_arr_l = sorted(div_arr_l, reverse=True)
        div_arr_b_one = sorted(div_arr_b_one, reverse=True)
        div_arr_b_pol = sorted(div_arr_b_pol, reverse=True)
        div_arr_b_two = sorted(div_arr_b_two, reverse=True)


        s_arr_cap = sorted(s_arr_cap, reverse=True)
        s_arr_l = sorted(s_arr_l, reverse=True)
        s_arr_b_one = sorted(s_arr_b_one, reverse=True)
        s_arr_b_pol = sorted(s_arr_b_pol, reverse=True)
        s_arr_b_two = sorted(s_arr_b_two, reverse=True)


        len_cap = []
        len_l = []
        len_b_one = []
        len_b_pol  = []
        len_b_two = []



        for i in range(1,len(div_arr_cap)):
            len_cap.append(i)
        for i in range(1,len(div_arr_l)):
            len_l.append(i)
        for i in range(1,len(div_arr_b_one)):
            len_b_one.append(i)
        for i in range(1,len(div_arr_b_pol)):
            len_b_pol.append(i)
        for i in range(1,len(div_arr_b_two)):
            len_b_two.append(i)

        a = len_cap[-1]
        b = len_l[-1]
        c = len_b_one[-1]
        d = len_b_pol[-1]
        e = len_b_two[-1]



        co_data = [a,b,c,d,e]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'len_d': len_cap,

                'div_arr_cap': div_arr_cap,
                'div_arr_l': div_arr_l,
                'div_arr_b_one': div_arr_b_one,
                'div_arr_b_pol': div_arr_b_pol,
                'div_arr_b_two': div_arr_b_two,

                's_arr_cap': s_arr_cap,
                's_arr_l': s_arr_l,
                's_arr_b_one': s_arr_b_one,
                's_arr_b_pol':s_arr_b_pol,
                's_arr_b_two':s_arr_b_two,


            }
        return JsonResponse(response)
    else:
        raise Http404


def add_ajaxfour(request):
    if request.is_ajax():
        items = GlassFridge.objects.all()
        #len_d = []
#diagonals
        div_arr_cap = []
        div_arr_cap_blue = []
        div_arr_cap_yellow = []

#sides
        s_arr_cap = []
        s_arr_cap_blue = []
        s_arr_cap_yellow = []
#longs of arrays


        for item in items:
            if item.label == "cap":
                div_arr_cap.append(float(item.diagonals))
                s_arr_cap.append(float(item.sides))
            if item.label == "yellow_cap":
                div_arr_cap_yellow.append(float(item.diagonals))
                s_arr_cap_yellow.append(float(item.sides))

            if item.label == "blue_cap":
                div_arr_cap_blue.append(float(item.diagonals))
                s_arr_cap_blue.append(float(item.sides))

        div_arr_cap = sorted(div_arr_cap, reverse=True)
        div_arr_cap_yellow = sorted(div_arr_cap_yellow, reverse=True)
        div_arr_cap_blue = sorted(div_arr_cap_blue, reverse=True)

        s_arr_cap = sorted(s_arr_cap, reverse=True)
        s_arr_cap_yellow = sorted(s_arr_cap_yellow, reverse=True)
        s_arr_cap_blue = sorted(s_arr_cap_blue, reverse=True)

        len_cap = []
        len_cap_blue = []
        len_cap_yellow = []

        for i in range(1,len(div_arr_cap)):
            len_cap.append(i)
        for i in range(1,len(div_arr_cap_blue)):
            len_cap_blue.append(i)
        for i in range(1,len(div_arr_cap_yellow)):
            len_cap_yellow.append(i)

        a = len_cap[-1]
        b = len_cap_blue[-1]
        c = len_cap_yellow[-1]

        co_data = [a,b,c]


        #co_data=[1,2,3,4,5,66]
        response = {
                'co_data':co_data,
                'len_d': len_cap,

                'div_arr_cap': div_arr_cap,
                'div_arr_cap_blue': div_arr_cap_blue,
                'div_arr_cap_yellow': div_arr_cap_yellow,

                's_arr_cap': s_arr_cap,
                's_arr_cap_blue': s_arr_cap_blue,
                's_arr_cap_yellow': s_arr_cap_yellow,

            }
        return JsonResponse(response)
    else:
        raise Http404

def add_ajaxfive(request):
    if request.is_ajax():
        items = GlassFridgeImages.objects.all()

        red_mean = []
        green_mean = []
        blue_mean = []
        overall_mean = []

        red_stand = []
        green_stand = []
        blue_stand = []
        overall_stand = []

        for item in items:
            red_mean.append(item.red_mean)
            green_mean.append(item.green_mean)
            blue_mean.append(item.blue_mean)
            overall_mean.append(item.overall_mean)

            red_stand.append(item.red_stand)
            green_stand.append(item.green_stand)
            blue_stand.append(item.blue_stand)
            overall_stand.append(item.overall_stand)

        #red_mean = sorted(red_mean, reverse=False)
        #green_mean = sorted(green_mean, reverse=False )
        #blue_mean = sorted(blue_mean, reverse=False)
        #overall_mean =sorted(overall_mean, reverse=False)
        #co_data=[1,2,3,4,5,66]

        #redTh = []
        #redFif = []
        #redSix = []

        for i in red_mean:
            if float(i) <= 40:
                redTh.append(i)
            if float(i) > 40 and float(i) <= 50:
                redFif.append(i)
            if float(i) > 50 and float(i) <= 60:
                redSix.append(i)
        response = {
                'red_mean': red_mean,
                'green_mean': green_mean,
                'blue_mean': blue_mean,
                'overall_mean': overall_mean,

                'red_stand': red_stand,
                'green_stand': green_stand,
                'blue_stand': blue_stand,
                'overall_stand': overall_stand,

                'redTh': redTh,
                'redFif': redFif,
                'redSix': redSix,

            }
        return JsonResponse(response)
    else:
        raise Http404


def add_ajaxsix(request):
    if request.is_ajax():
        items = PhilipMorris.objects.all()

        PhilipMorrisBlue_dia = []
        PhilipMorrisBlue25_dia = []
        PhilipMorrisGold_dia = []
        PhilipMorrisNovelBlue_dia = []
        PhilipMorrisNovelMix_dia = []
        PhilipMorrisNovelRed_dia = []
        PhilipMorrisNovelSilver_dia = []
        PhilipMorrisRed_dia = []
        PhilipMorrisRed25_dia = []
        PhilipMorrisRedKingSize_dia = []

        ParliamentAquaBlue_dia = []
        ParliamentCaratBlue_dia = []
        ParliamentCaratPurple_dia = []
        ParliamentNightBlue_dia = []
        ParliamentPearlBlue_dia = []
        ParliamentPlatinum_dia = []
        ParliamentSilverBlue_dia = []
        ParliamentSilverSuperSlims_dia = []
        ParliamentAquaSuperSlims_dia = []

        NextPink_dia = []
        NextViolet_dia = []


        BondBlue6_dia = []
        BondBlueSelection_dia = []
        BondBlueSelection25_dia = []
        BondPremiumMix_dia = []
        BondPremiumSilver_dia = []
        BondRedSelection_dia = []
        BondRedSelection25_dia = []
        BondSilverClassic_dia = []
        BondSilverClassic25_dia = []
        BondBlue6_2019_dia = []
        BondBlueSelection_2019_dia = []
        BondBlueSelection25_2019_dia = []
        BondPremiumSilver_2019_dia = []
        BondRedSelection_2019_dia = []
        BondRedSelection25_2019_dia = []
        BondSilverClassic_2019_dia = []
        BondSilverClassic25_2019_dia= []

        ChesterfieldKSBlue_dia = []
        ChesterfieldKSBronze_dia = []
        ChesterfieldKSRed_dia = []

        LMBlueLabel_dia = []
        LMFineCutSilver_dia = []
        LMLoftBlue_dia = []
        LMLoftDoubleSplash_dia = []
        LMLoftMix_dia = []
        LMLoftNightBlue_dia = []
        LMLoftSeaBlue_dia = []
        LMSmartSeriesRed_dia = []

        MarlboroFineTouchLightBlue_dia = []
        MarlboroFlavorMix_dia = []
        MarlboroGold_dia = []
        MarlboroMicro_dia = []
        MarlboroRed_dia = []
        MarlboroSilver_dia = []
        MarlboroTouchBlue_dia = []

        MurattiGreen_dia = []
        MurattiPeach_dia = []
        MurattiPink_dia = []
        MurattyViolet_dia = []


        for item in items:
            #philipmorris
            if item.label == "PhilipMorrisBlue":
                PhilipMorrisBlue_dia.append(item.diagonals)
            if item.label == "PhilipMorrisBlue25":
                PhilipMorrisBlue25_dia.append(item.diagonals)
            if item.label == "PhilipMorrisGold":
                PhilipMorrisGold_dia.append(item.diagonals)
            if item.label == "PhilipMorrisNovelBlue":
                PhilipMorrisNovelBlue_dia.append(item.diagonals)
            if item.label == "PhilipMorrisNovelMix":
                PhilipMorrisNovelMix_dia.append(item.diagonals)
            if item.label == "PhilipMorrisNovelRed":
                PhilipMorrisNovelRed_dia.append(item.diagonals)
            if item.label == "PhilipMorrisNovelSilver":
                PhilipMorrisNovelSilver_dia.append(item.diagonals)
            if item.label == "PhilipMorrisRed":
                PhilipMorrisRed_dia.append(item.diagonals)
            if item.label == "PhilipMorrisRed25":
                PhilipMorrisRed25_dia.append(item.diagonals)
            if item.label == "PhilipMorrisRedKingSize":
                PhilipMorrisRedKingSize_dia.append(item.diagonals)

            #parlament
            if item.label == "ParliamentAquaBlue":
                ParliamentAquaBlue_dia.append(item.diagonals)
            if item.label == "ParliamentCaratBlue":
                ParliamentCaratBlue_dia.append(item.diagonals)
            if item.label == "ParliamentCaratPurple":
                ParliamentCaratPurple_dia.append(item.diagonals)
            if item.label == "ParliamentNightBlue":
                ParliamentNightBlue_dia.append(item.diagonals)
            if item.label == "ParliamentPearlBlue":
                ParliamentPearlBlue_dia.append(item.diagonals)
            if item.label == "ParliamentPlatinum":
                ParliamentPlatinum_dia.append(item.diagonals)
            if item.label == "ParliamentSilverBlue":
                ParliamentSilverBlue_dia.append(item.diagonals)
            if item.label == "ParliamentSilverSuperSlims":
                ParliamentSilverSuperSlims_dia.append(item.diagonals)
            if item.label == "ParliamentAquaSuperSlims":
                ParliamentAquaSuperSlims_dia.append(item.diagonals)
            #next

            if item.label == "NextPink":
                NextPink_dia.append(item.diagonals)
            if item.label == "NextViolet":
                NextViolet_dia.append(item.diagonals)

            #bond
            if item.label == "BondBlue#6":
                BondBlue6_dia.append(item.diagonals)
            if item.label == "BondBlueSelection":
                BondBlueSelection_dia.append(item.diagonals)
            if item.label == "BondBlueSelection25":
                BondBlueSelection25_dia.append(item.diagonals)
            if item.label == "BondPremiumMix":
                BondPremiumMix_dia.append(item.diagonals)
            if item.label == "BondPremiumSilver":
                BondPremiumSilver_dia.append(item.diagonals)
            if item.label == "BondRedSelection":
                BondRedSelection_dia.append(item.diagonals)
            if item.label == "BondRedSelection25":
                BondRedSelection25_dia.append(item.diagonals)
            if item.label == "BondSilverClassic":
                BondSilverClassic_dia.append(item.diagonals)
            if item.label == "BondSilverClassic25":
                BondSilverClassic25_dia.append(item.diagonals)
            if item.label == "BondBlue#6_2019":
                BondBlue6_2019_dia.append(item.diagonals)
            if item.label == "BondBlueSelection_2019":
                BondBlueSelection_2019_dia.append(item.diagonals)
            if item.label == "BondBlueSelection25_2019":
                BondBlueSelection25_2019_dia.append(item.diagonals)
            if item.label == "BondPremiumSilver_2019":
                BondPremiumSilver_2019_dia.append(item.diagonals)
            if item.label == "BondRedSelection_2019":
                BondRedSelection_2019_dia.append(item.diagonals)
            if item.label == "BondRedSelection25_2019":
                BondRedSelection25_2019_dia.append(item.diagonals)
            if item.label == "BondSilverClassic_2019":
                BondSilverClassic_2019_dia.append(item.diagonals)
            if item.label == "BondSilverClassic25_2019":
                BondSilverClassic25_2019_dia.append(item.diagonals)
            #chester
            if item.label == "ChesterfieldKSBlue":
                ChesterfieldKSBlue_dia.append(item.diagonals)
            if item.label == "ChesterfieldKSBronze":
                ChesterfieldKSBronze_dia.append(item.diagonals)
            if item.label == "ChesterfieldKSRed":
                ChesterfieldKSRed_dia.append(item.diagonals)
            #lM
            if item.label == "LMBlueLabel":
                LMBlueLabel_dia.append(item.diagonals)
            if item.label == "LMFineCutSilver":
                LMFineCutSilver_dia.append(item.diagonals)
            if item.label == "LMLoftBlue":
                LMLoftBlue_dia.append(item.diagonals)
            if item.label == "LMLoftDoubleSplash":
                LMLoftDoubleSplash_dia.append(item.diagonals)
            if item.label == "LMLoftMix":
                LMLoftMix_dia.append(item.diagonals)
            if item.label == "LMLoftNightBlue":
                LMLoftNightBlue_dia.append(item.diagonals)
            if item.label == "LMLoftSeaBlue":
                LMLoftSeaBlue_dia.append(item.diagonals)
            if item.label == "LMSmartSeriesRed":
                LMSmartSeriesRed_dia.append(item.diagonals)

            #marlboro
            if item.label == "MarlboroFineTouchLightBlue":
                MarlboroFineTouchLightBlue_dia.append(item.diagonals)
            if item.label == "MarlboroFlavorMix":
                MarlboroFlavorMix_dia.append(item.diagonals)
            if item.label == "MarlboroGold":
                MarlboroGold_dia.append(item.diagonals)
            if item.label == "MarlboroMicro":
                MarlboroMicro_dia.append(item.diagonals)
            if item.label == "MarlboroRed":
                MarlboroRed_dia.append(item.diagonals)
            if item.label == "MarlboroSilver":
                MarlboroSilver_dia.append(item.diagonals)
            if item.label == "MarlboroTouchBlue":
                MarlboroTouchBlue_dia.append(item.diagonals)
            #muratti
            if item.label == "MurattiGreen":
                MurattiGreen_dia.append(item.diagonals)
            if item.label == "MurattiPeach":
                MurattiPeach_dia.append(item.diagonals)
            if item.label == "MurattiPink":
                MurattiPink_dia.append(item.diagonals)
            if item.label == "MurattyViolet":
                MurattyViolet_dia.append(item.diagonals)




        #red_mean = sorted(red_mean, reverse=False)
        #green_mean = sorted(green_mean, reverse=False )
        #blue_mean = sorted(blue_mean, reverse=False)
        #overall_mean =sorted(overall_mean, reverse=False)
        #co_data=[1,2,3,4,5,66]


        NumberOfSigaretsArray =[len(PhilipMorrisBlue_dia),
        len(PhilipMorrisBlue25_dia),
        len(PhilipMorrisGold_dia),
        len(PhilipMorrisNovelBlue_dia),
        len(PhilipMorrisNovelMix_dia ),
        len(PhilipMorrisNovelRed_dia),
        len(PhilipMorrisNovelSilver_dia),
        len(PhilipMorrisRed_dia),
        len(PhilipMorrisRed25_dia),
        len(PhilipMorrisRedKingSize_dia),

        len(ParliamentAquaBlue_dia),
        len(ParliamentCaratBlue_dia),
        len(ParliamentCaratPurple_dia),
        len(ParliamentNightBlue_dia),
        len(ParliamentPearlBlue_dia),
        len(ParliamentPlatinum_dia),
        len(ParliamentSilverBlue_dia),
        len(ParliamentSilverSuperSlims_dia),
        len(ParliamentAquaSuperSlims_dia),

        len(NextPink_dia),
        len(NextViolet_dia),
        len(BondBlue6_dia),
        len(BondBlueSelection_dia),
        len(BondBlueSelection25_dia),
        len(BondPremiumMix_dia),
        len(BondPremiumSilver_dia),
        len(BondRedSelection_dia),
        len(BondRedSelection25_dia),
        len(BondSilverClassic_dia),
        len(BondSilverClassic25_dia),
        len(BondBlue6_2019_dia),
        len(BondBlueSelection_2019_dia),
        len(BondBlueSelection25_2019_dia),
        len(BondPremiumSilver_2019_dia),
        len(BondRedSelection_2019_dia),
        len(BondRedSelection25_2019_dia),
        len(BondSilverClassic_2019_dia),
        len(BondSilverClassic25_2019_dia),

        len(ChesterfieldKSBlue_dia),
        len(ChesterfieldKSBronze_dia),
        len(ChesterfieldKSRed_dia),


        len(LMBlueLabel_dia),
        len(LMFineCutSilver_dia),
        len(LMLoftBlue_dia),
        len(LMLoftDoubleSplash_dia),
        len(LMLoftMix_dia),
        len(LMLoftNightBlue_dia),
        len(LMLoftSeaBlue_dia),
        len(LMSmartSeriesRed_dia),

        len(MarlboroFineTouchLightBlue_dia),
        len(MarlboroFlavorMix_dia),
        len(MarlboroGold_dia),
        len(MarlboroMicro_dia),
        len(MarlboroRed_dia),
        len(MarlboroSilver_dia),
        len(MarlboroTouchBlue_dia),

        len(MurattiGreen_dia),
        len(MurattiPeach_dia),
        len(MurattiPink_dia),
        len(MurattyViolet_dia),


        ]




        response = {
                'NumberOfSigaretsArray':NumberOfSigaretsArray,


            }
        return JsonResponse(response)
    else:
        raise Http404
