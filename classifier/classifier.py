from transformers import pipeline

class TweetClassifier:
    def __init__(self, model_name, tokenizer_name):
        """
        Initializes the classifier with the given model and tokenizer.
        """
        self.classifier = pipeline(
            "text-classification",
            model=model_name,
            tokenizer=tokenizer_name
        )

    def classify(self, text):
        """
        Classifies the given text and returns the label and confidence score.
        
        Args:
            text (str): The text to classify.
        
        Returns:
            dict: A dictionary containing the label and confidence score.
        """
        if not text.strip():
            raise ValueError("Input text cannot be empty.")
        
        prediction = self.classifier(text)
        return prediction[0]  # Return the first (and only) prediction
