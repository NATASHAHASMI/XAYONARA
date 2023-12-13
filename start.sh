if [ -z "$UPSTREAM_REPO" ]; then
  echo "Cloning main Repository"
  git clone https://github.com/1238muj/THALAPATHY-FILTER-BOT.git /THALAPATHY-FILTER-BOT
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone "$UPSTREAM_REPO" /THALAPATHY-FILTER-BOT
fi

cd /THALAPATHY-FILTER-BOT || exit

pip install -U -r requirements.txt

echo "Starting Bot..."
python3 bot.py
