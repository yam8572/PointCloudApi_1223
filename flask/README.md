## template1 dockerfile+flask

詳細設定寫於：
[實作 Dockerfile + flask 教學 (附GitHub完整程式) | Max行銷誌](https://www.maxlist.xyz/2020/01/11/docker-flask/)

### step 1 - git clone
``` 
git clone https://github.com/yam8572/pointcloudapi.git
cd pointcloudapi
```

### step 2 -  將 dockerfile 打包成 image
## Wait for build sucess. (Takes 15 mins each, due to the open3d installation)
``` 
docker image build -t image_pointcloud .
```

### step 3 - 透過 image 產生隔離的執行環境 container

``` 
docker run -p 80:8888 --name pointcloudapi image_pointcloud
```

連線 0.0.0.0:80 或 127.0.0.1:80 

# 說明 <br>
1.透過python的image去啟動<br>
2.先進入app/ folder，將本機上面這些檔案複製上去<br>
3.install必要的package，接著就透過uwsgi去啟動服務<br>

main.py: flask主程式<br>
requirements.txt: 需要套件library<br>
wsgi.ini: uwsgi的設定<br>
