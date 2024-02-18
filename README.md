# Advanced Lifespan Intelligence Virtual Expert (ALIVE)

## Summary

ALIVE is an artificial intelligence-based recommendation system for longevity supplementation and drug repurposing. Based on your unique biological profile, ALIVE will recommend a personalized regimen of supplements and drugs to optimize your healthspan. ALIVE places control over your healthspan into your own hands.

Built for [TreeHacks 2024](https://www.treehacks.com/) at Stanford University.

## Problem Statement 💡



## Large Language Model ✨

The large language model (LLM) that underlies ALIVE was initialized from [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) and was fine-tuned using [Monster API](https://monsterapi.ai/) on the filtered [DrugAge database](https://genomics.senescence.info/drugs/), a database of aging related drugs. We used the following prompt for fine-tuning:

```
You are an expert drug development scientist and biomedical researcher studying drugs that can promote longevity and extend healthspan. You must answer an important question. Generate a response that answers this question.

###Question: If you administer the compound {compound_name} in a {species} {strain} {gender} model organism at {dosage} dosage, what will the average lifespan change be in years?

###Response: The average lifespan change will be {avg_lifespan_change} years.
```

Training results are available via Weights & Biases at [this dashboard](https://api.wandb.ai/links/ayushnoori/9xquz6sq).

## Future Directions 🚀

TBD

## Base Dependencies 📦 

TBD

## Development Team 🧑‍💻
* [Ayush Noori](mailto:anoori@college.harvard.edu)
* [Sibi Raja](mailto:sraja@college.harvard.edu)
* [Jay Iyer](mailto:sraja@college.harvard.edu)

This project was completed during the [TreeHacks 2024](https://www.treehacks.com/) hackathon at Stanford University.

## References 📚

