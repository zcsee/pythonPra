from caseconverter import pascalcase

wait_for_convert = [{
    "clip_end": 4.929166793823242,
    "clip_start": 1.5,
    "endtime": 3.429166078567505,
    "height": 0,
    "source": "",
    "starttime": 0,
    "type": "video",
    "uuid": "167170120247933694724828150192",
    "volume": 1,
    "width": 0
},
    {
        "clip_end": 4.916666030883789,
        "clip_start": 0,
        "endtime": 7.666666030883789,
        "height": 0,
        "source": "",
        "starttime": 2.75,
        "type": "video",
        "uuid": "167170120247945294724828725952",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 4.8333330154418945,
        "clip_start": 0,
        "endtime": 12.375,
        "height": 0,
        "source": "",
        "starttime": 7.541666030883789,
        "type": "video",
        "uuid": "167170120247951894724827717680",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 5,
        "clip_start": 0,
        "endtime": 17.33333396911621,
        "height": 0,
        "source": "",
        "starttime": 12.333333015441895,
        "type": "video",
        "uuid": "167170120247958394724827792400",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 6.041666030883789,
        "clip_start": 0,
        "endtime": 23.08333396911621,
        "height": 0,
        "source": "",
        "starttime": 17.04166603088379,
        "type": "video",
        "uuid": "167170120247968794724828317600",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 4.920000076293945,
        "clip_start": 0.5833330154418945,
        "endtime": 26.003334045410156,
        "height": 0,
        "source": "",
        "starttime": 21.66666603088379,
        "type": "video",
        "uuid": "167170120247976294724828578816",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 5.916666030883789,
        "clip_start": 0,
        "endtime": 31.29166603088379,
        "height": 0,
        "source": "",
        "starttime": 25.375,
        "type": "video",
        "uuid": "167170120247982494724827787200",
        "volume": 1,
        "width": 0
    },
    {
        "clip_end": 5.166666030883789,
        "clip_start": 0,
        "endtime": 35.79166793823242,
        "height": 0,
        "source": "",
        "starttime": 30.625,
        "type": "video",
        "uuid": "167170120247988794724828251920",
        "volume": 1,
        "width": 0
    }]

for kk in wait_for_convert.pop().keys():
    print(pascalcase(kk))
