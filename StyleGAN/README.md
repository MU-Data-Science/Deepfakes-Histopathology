# Pathology-GAN
PathologyGAN aims to capture key tissue features and uses these characteristics to give structure to its latent space. It uses BigGAN as its baseline architecture to build a latent space of key tissue features. In addition to it, it also incorporates advances from StyleGAN to optimize this latent space in order to identify features of cancerous tissues. The model also replaces Hinge loss with Relativistic Average Discriminator as the GAN objective to enable faster convergence and help capture morphological structure of tissues accurately.

## To train Pathology-GAN
1. Clone the Pathology-GAN Repository
    ```
    git clone https://github.com/AdalbertoCq/Pathology-GAN.git
    ```
2. Install the required libraries.
    ```
    pip install -r requirements.txt
    ```
3. Split the input patches into train and test sets.
    ```
    python split_data.py -data <PATCHES_DIR>
    ```
    eg: `python split_data.py -data colon-patches`
4. Create the dataset directory inside Pathology-GAN
    ```
    mkdir -p Pathology-GAN/dataset/vgh_nki/he/patches_h224_w224
    ```
5. Create input data for PathologyGAN
    ```
    python createh5.py -train <TRAIN_DIR> -test <TEST_DIR> -out <OUT_DIR>
    ```
    eg: `python createh5.py -train colon-patches-train -test colon-patches-test -out Pathology-GAN/dataset/vgh_nki/he/patches_h224_w224`
6. To train PathologyGAN
    ```
    cd Pathology-GAN && python run_pathgan.py --epochs <EPOCHS>
    ```

## References
* [Pathology-GAN](https://openreview.net/pdf?id=CwgSEEQkad)
* [Pathoglogy-GAN Github Repository](https://github.com/AdalbertoCq/Pathology-GAN)