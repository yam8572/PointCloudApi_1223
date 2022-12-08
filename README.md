# Point Cloud Api
點雲後端

# git push  
1.新建本地數據庫（Local Repository 只需要新建一次就好）
git init
2.將檔案移入索引中
git add .
3.將索引內的檔案提交至本地數據庫
git commit -m "添加commit的說明"
4.先自行新建好 GitHub 的 Repository，開啟終端機，在該目錄下輸入以下指令
(不」打勾 "Initialize this repository with a README")

git remote -v

錯誤
remote origin already exists
git remote rm origin
git remote add origin git@github.com:yam8572/PointCloudApi.git
# 分支
git branch -M main
git push -u origin main

這段訊息的意思是線上版本的內容比你電腦裡這份還要新，所以 Git 不讓你推上去。
error: failed to push
第一招：先拉再推
因為你電腦裡的內容是比較舊的，所以你應該先拉一份線上版本的回來更新，然後再推一次：
git pull --rebase
第二招：強制推蓋過去
git push -f origin main
