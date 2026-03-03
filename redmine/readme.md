


## auto_close_foreach_list
用来自动关闭“工时日志”中的任务。

原理就是模拟人的操作，打开浏览器，登录，点击任务详情，找到修改状态的按钮，修改为“已关闭”


用到的技术

* selenium 一个自动化测试的框架
* msedgedriver edge的浏览器驱动，它提供一套api可以访问浏览器


使用方法：

* 手动登录redmine，打开F12获取cookie信息：_redmine_session  和 autologin，然后填写到如下位置：

```

   # 设置 cookies
    cookies = [
        {
            "name": "_redmine_session",
            "value": "NkM5a0Z0Y2E1L3RTZW1QSTV5TVJ3dkdJeVZqdDhtQzhOYW1rK1VwSGRlOXJSd3IvaU16WHVGWEF4VGJMMDNZb05zemtqQW5QZmFWMmlLSDIzejg5VVdHR1VWTm8yQlV1NHRrTmRnK3AzdmtGWmxuejlNMjk2TlhEWW1UUG15UlFPdWZqWHJCNjNpblR2RGhleXZlbyt1aFFWTDE5alhyb3RoSXgyQ1hPTFdqWkM3VEdxT2FsdmJEaUxNRUk1dlVCcFZYRC9OQUVMQ3l4RzArNkpzTHlpVGc2bUtKNHpWWWFXQlRwOHpWb2pEc3B4U1lWVE5GUFVCQURkR1lGOFgrbjZEc2tZK3J5ZWhHL2NiQTZkaXJlU21FeFRCVnhKNHg2RUM4WGdGcUY3UStPb3lESm5rVXU5VDZpQmpuNnVFc2hZeHplaHlrbVloMjkyekYzanY0bTBGbzExWXNUR0NEejArcERvbnQxWEhPeER5anptMFBuSks5bGVqTVM4RVk3RHdHMzlmMk9xRUhWT0pyNlVzNkJ1MlQ0aGh2dkxNM2lNelVQVVVVbkNUNmwyMEh1UWZDYzZmQ091aWFyVEF0NHN4QWpMUjR2S0VkR29jWm5pV3hpb3cxSkRPQWdBcnEwTWFVWEl2V2xZci91MDQ3elRhTHdNMkFyN0dxYndoSFYtLVFEOHI3YWhIK3grdFg1NzZvejFpNnc9PQ%3D%3D--08e15c197e0e8e08a55881d86982847f1442af54",
        },
        {"name": "autologin", "value": "38f91daedd7083c73ecc7c104a3bf86da40e183d"},
    ]

```

* 设置任务页面，先点击工时日志，再选择一个项目，这样“日报告”列表将仅显示此项目下的未关闭任务，然后程序通过遍历任务，模拟点击任务详情，模拟点击编辑按钮，模拟修改任务状态为“已关闭”

```

http://demo.nghinsights.com:1234/redmine/work_time/index?day=3&month=3&prj=491&user=122&year=2026

```

注意事项，edge浏览器若是自动更新的话，会出现edge版本和msedgedriver版本不一致问题，此时将报如下异常

```
Exception has occurred: SessionNotCreatedException
Message: session not created: This version of Microsoft Edge WebDriver only supports Microsoft Edge version 142
Current browser version is 145.0.3800.82 with binary path C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe

```

解决办法就是下载和edge浏览器配套的msedgedriver，它俩版本号规则一样，下载地址：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads


当前待解决的问题

* 需要手动选择一个项目，后续想优化成用户设置“工时日志”页面的地址作为任务页面。