# Pathology-GAN
StyleGAN extends the traditional GAN architecture by incorporating changes to the generator model including the use of a non-linear mapping network that mapped points in latent space to an intermediate latent space. Stochastic variation was introduced through noise added at each point in the generator model that enabled finer interpretation of the style of the generated image. 

## To train Pathology-GAN
1. Clone the StyleGAN Repository
    ```
    git clone https://github.com/NVlabs/stylegan.git
    ```
2. Install the required libraries.
    ```
    pip3 install -r requirements.txt
    ```
3. Create Datasets directory inside StyleGAN
    ```
    mkdir -p Datasets    
    ```
4. Create histopathologyImages & histopathologyTFRecords directories inside Datasets
    ```
    mkdir -p  histopathologyImages
    mkdir -p  histopathologyTFRecords

    ```
5. Copy your training images to Datasets/histopathologyImages
    ```
    cp training/images Datasets/histopathologyImages
    ```

6. Prepare the dataset for training
    ```
    python3 dataset_tool.py create_from_images path/to/TFRecords path/to/training/images
    ```
    eg: `python3 dataset_tool.py create_from_image Datasets/histopathologyTFRecords Datasets/histopathologyImages `
7. To train SyleGAN
   Edit the ```train.py``` to specify the dataset and training configuration
   ```
   python3 train.py 
   ```

## References
* [StyleGAN](https://arxiv.org/abs/1812.04948)
* [StyleGAN Github Repository](https://github.com/NVlabs/stylegan)