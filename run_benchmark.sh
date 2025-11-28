for task in "risk" "stocktweets"
# "news" "finphrase" "risk" "secfilings" "fiqa" "stocktweets"
do
    for model in "yannikmaassen/BusinessBERT2-v1-70000" "yannikmaassen/BusinessBERT2-v1-1000000"
    # "pborchert/BusinessBERT" "bert-base-uncased" "yiyanghkust/finbert-pretrain" "ProsusAI/finbert"
    do
        for seed in 42
        do
            python3 businessbench.py \
            --task_name $task \
            --model_name $model \
            --seed $seed
        done
    done
done