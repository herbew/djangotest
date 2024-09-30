#|==============================================================================
#|          D E P L O Y M E N T   G U I D A N C E with Ubuntu 22.04
#|==============================================================================

sudo apt-get install build-essential checkinstall
sudo apt-get install libncursesw5-dev libssl-dev libpq-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev

sudo apt install firefox

sudo apt-get install language-pack-id
sudo dpkg-reconfigure locales

sudo apt-get install -y python3 python3-pip 
sudo apt-get install -y python3-venv

python3 -m venv envdjangopytest

git clone https://github.com/herbew/djangotest.git

cd djangotest
pip install -r requirements.txt
