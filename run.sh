export CUDA_VISIBLE_DEVICES=2,3
python3 src/main.py --model Llama-3.1-8B-Instruct > main.log 2>&1 &