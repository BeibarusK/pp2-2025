#git config --global user.name "Your Name"
#git config --global user.email "your_email@whatever.com"
#git config --global init.defaultBranch main
#git config --global core.autocrlf input
#git config --global core.safecrlf warn
#git config --global core.autocrlf true
#git config --global core.safecrlf warn
#mkdir work
#cd work
#touch hello.html
#git add hello.html
#git commit -m "Initial Commit"
#git status
#git add a.html
#git add b.html
#git commit -m "Changes for a and b"
#git commit
#git commit -m "Added standard HTML page tags"
#git status
#git add .
#git status
#git commit -m "Added HTML header"
#git log
#git log --pretty=oneline
#git log --oneline --max-count=2
#git log --oneline --since="5 minutes ago"
#git log --oneline --until="5 minutes ago"
#git log --oneline --author="Your Name"
#git log --oneline --all
#git log --all --pretty=format:"%h %cd %s (%an)" --since="7 days ago"
#git log --pretty=format:"%h %ad | %s%d [%an]" --date=short
#git config --global format.pretty '%h %ad | %s%d [%an]'
#git config --global log.date short
#git checkout <hash>
#cat hello.html
#git switch main
#cat hello.html
#git tag v1
#git log
#git checkout v1^
#cat hello.html
#git tag v1-beta
#git log
#git checkout v1
#git checkout v1-beta
#git tag
#git log main --all
#git log main --all
#git tag -d oops
#git log --all
#git add style.css
#git commit -m "Added css stylesheet"
#mkdir css
#git mv style.css css/style.css
#git status
#git commit -m "Renamed hello.html; moved style.css"
#git log css/style.css
#git log --follow css/style.css
#git switch main
#git add README
#git commit -m "Added README"
#git log --all --graph
#git switch style
#git merge main
#git log --all --graph
#git switch style
#git rebase main
#git status
#git clone work home
#ls
#cd ../home
#git fetch
#git log --all
#git remote add shared ../work.git
#git branch --track shared main
#git pull shared main
#cat README