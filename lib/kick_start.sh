cron
cd /root/app
python3 run.py &
python3 convert.py &

while true
do
	sleep 1
done