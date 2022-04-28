export PYTHONPATH=$PYTHONPATH:`pwd`
main=$(find . -name "show_world_generation.py")
python3 $main
