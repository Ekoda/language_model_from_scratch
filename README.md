# EssentialTransformer
The Transformer model has revolutionized the field of natural language processing, enabling state-of-the-art results in tasks like translation, summarization, and much more. Yet, for those new to the field, the architecture can seem daunting.

EssentialTransformer is an exploration into the intricate workings of the Transformer model. Built entirely from scratch using only Numpy. This project is all about building intuition and understanding of the fundamental concepts that underpin the Transformer architecture. The focus is not to be the fastest or most optimized model. Instead its aim is to be clear and educational for those wanting to understand the technical details of how transformers work.

The project breaks down the Transformer into its core components, implementing each piece separately using Numpy. The focus is on code that is easy to understand and learn from, so you can see exactly how each piece of the puzzle fits together.


#### Project Structure
The project is structured in a hierarchical and modular fashion according to the original "attention is all you need" paper (Vaswani et al., 2017). As such the code in the components folder contain most of the detail, while code such as the transformer.py and decoder.py focus mainly on tying all the pieces together.

```
root/
├── src/
│   └── utils/
│   └── transformer/
│        └── components/
│        └── preprocessing/
│        └── transformer.py
│        └── decoder.py
└── tests/
```