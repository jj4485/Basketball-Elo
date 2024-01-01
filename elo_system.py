class EloRatingSystem:
    def __init__(self, a_rating, b_rating, winner, k_factor = 32, c = 400):
        self.a_rating = a_rating
        self.b_rating = b_rating
        self.winner = winner
        self.k_factor = k_factor
        self.c = c
        if (winner == 'a'):
            self.sa = 1
            self.sb = 0
        if (winner == 'b'):
            self.sb = 1
            self.sa = 0 

    def expected_outcome(self):
        a_exponent = self.a_rating / self.c
        Qa = 10 ** a_exponent
        b_exponent = self.b_rating / self.c
        Qb = 10 ** b_exponent
        expected_outcome_a = (Qa) / (Qa + Qb)
        expected_outcome_b = (Qb) / (Qa + Qb)
        return [expected_outcome_a, expected_outcome_b]

    
    def generate_new_ratings_a(self):
        ea = self.expected_outcome()[0]
        new_a_rating = self.a_rating + self.k_factor * (self.sa - ea)
        return new_a_rating
    
    def generate_new_ratings_b(self):
        eb = self.expected_outcome()[1]
        new_b_rating = self.b_rating + self.k_factor * (self.sb - eb)
        return new_b_rating
    
def main():
    rating = EloRatingSystem(1000, 3000, 'b')
    print(rating.generate_new_ratings_a())
    print(rating.generate_new_ratings_b())

if __name__ == "__main__":
    main()
        
        
