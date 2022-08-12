
#sudo apt-get install dos2unix
#sudo apt install ruby-full

mkdir -p sourceFiles/sparkfun
cd sourceFiles/sparkfun
#for i in 1 2 3 4 5 6 7 8 9 10 11 12 
#do
#    sudo curl -s "https://api.github.com/orgs/sparkfun/repos?per_page=100&page=$i" | ruby -rrubygems -e 'require "json"; JSON.load(STDIN.read).each { |repo| %x[git clone #{repo["clone_url"]} ]}'
#done
cd ..
mkdir -p adafruit
cd adafruit
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
do
    curl -s "https://api.github.com/orgs/adafruit/repos?per_page=100&page=$i" | ruby -rrubygems -e 'require "json"; JSON.load(STDIN.read).each { |repo| %x[git clone #{repo["clone_url"]} ]}'
done

