# Advanced Lifespan Intelligence Virtual Expert (ALIVE)

## Summary

ALIVE is an artificial intelligence-based recommendation system for longevity supplementation and drug repurposing. Based on your unique biological profile, ALIVE will recommend a personalized regimen of supplements and drugs to optimize your healthspan. ALIVE places control over your healthspan into your own hands. 

Built for [TreeHacks 2024](https://www.treehacks.com/) at Stanford University.

## Problem Statement 💡
As we turn to the future, aging is one of the most pressing challenges facing healthcare systems today. This effect is especially seen in Japan, where one in 10 people are now aged 80 years of age or older. 


## Large Language Model ✨

The large language model (LLM) that underlies ALIVE was initialized from [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) and was fine-tuned using [Monster API](https://monsterapi.ai/) on the filtered [DrugAge database](https://genomics.senescence.info/drugs/), a database of aging related drugs. We used the following prompt for fine-tuning:

```
You are an expert drug development scientist and biomedical researcher studying drugs that can promote longevity and extend healthspan. You must answer an important question. Generate a response that answers this question.

###Question: If you administer the compound {compound_name} in a {species} {strain} {gender} model organism at {dosage} dosage, what will the average lifespan change be in years?

###Response: The average lifespan change will be {avg_lifespan_change} years.
```

### Training Results 📈

Training results are available via Weights & Biases at [this dashboard](https://api.wandb.ai/links/ayushnoori/9xquz6sq).


### HuggingFace Release 🤗

Our fine-tuned large language model was released publicly with a detailed model card at the following HuggingFace link: [ayushnoori/alive](https://huggingface.co/ayushnoori/alive).


## Future Directions 🚀

In the future, we intend to use a deep learning model trained by jointly learning molecular structures and textual descriptions to improve the quality and accuracy of our recommendations. For example, we could use MoleculeSTM, a multi-modal molecule structure–text model trained on over 280,000 chemical structure–text pairs. For more details, please see the associated paper in *Nature Machine Intelligence*:
> Liu, S. et al. Multi-modal molecule structure–text model for text-based retrieval and editing. *Nat Mach Intell* **5**, 1447–1457 (2023). doi: [10.1038/s42256-023-00759-6](https://doi.org/10.1038/s42256-023-00759-6)

## Base Dependencies 📦 

TBD

## Development Team 🧑‍💻
* [Ayush Noori](mailto:anoori@college.harvard.edu)
* [Sibi Raja](mailto:sraja@college.harvard.edu)
* [Jay Iyer](mailto:sraja@college.harvard.edu)

This project was completed during the [TreeHacks 2024](https://www.treehacks.com/) hackathon at Stanford University.

## References 📚

