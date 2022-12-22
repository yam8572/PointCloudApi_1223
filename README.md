# Point Cloud Api
點雲後端

# git push  
1.新建本地數據庫（Local Repository 只需要新建一次就好）<br>
git init<br>
2.將檔案移入索引中<br>
git add .<br>
3.將索引內的檔案提交至本地數據庫<br>
git commit -m "添加commit的說明"<br>
4.先自行新建好 GitHub 的 Repository，開啟終端機，在該目錄下輸入以下指令<br>
(不」打勾 "Initialize this repository with a README")<br>

git remote -v<br>

錯誤 <br>
remote origin already exists<br>
git remote rm origin<br>
git remote add origin git@github.com:yam8572/PointCloudApi.git<br>

分支<br>
git branch -M main<br>
git push -u origin main<br>

這段訊息的意思是線上版本的內容比你電腦裡這份還要新，所以 Git 不讓你推上去。<br>
error: failed to push<br>
第一招：先拉再推<br>
因為你電腦裡的內容是比較舊的，所以你應該先拉一份線上版本的回來更新，然後再推一次：<br>
git pull --rebase<br>
第二招：強制推蓋過去<br>
git push -f origin main<br>
push test<br>
