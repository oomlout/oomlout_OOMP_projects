
#sudo apt-get update
#sudo apt-get install dos2unix
#sudo apt install ruby-full

#sudo dos2unix sourcePull.sh

cd sourceFiles

for org in "sparkfun" "adafruit"
do
	mkdir -p $org
	cd $org
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
	do
	    curl -s "https://api.github.com/users/$org/repos?per_page=100&page=$i" | ruby -rrubygems -e 'require "json"; JSON.load(STDIN.read).each { |repo| %x[git clone #{repo["clone_url"]} ]}'
	done
	cd ..
done


for org in "omerk" "electrolama"
do
	mkdir -p $org
	cd $org
	for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
	do
	    curl -s "https://api.github.com/users/$org/repos?per_page=100&page=$i" | ruby -rrubygems -e 'require "json"; JSON.load(STDIN.read).each { |repo| %x[git clone #{repo["clone_url"]} ]}'
	done
	cd ..
done

