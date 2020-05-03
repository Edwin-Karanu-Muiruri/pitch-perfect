class Review:
    all_reviews = []
    def __init__(self,pitch_id,title,review):
        self.pitch_id = pitch_id
        self.title = title
        self.review = review

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()