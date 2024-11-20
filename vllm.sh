export CUDA_VISIBLE_DEVICES=0,1,2,3
nohup vllm serve "meta-llama/Llama-3.1-70B-Instruct" --pipeline-parallel-size 4 --max_model_len 50000 > vllm.log 2>&1 &