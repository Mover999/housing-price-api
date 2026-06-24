from sklearn.base import BaseEstimator, TransformerMixin

class HousingFeatEng(BaseEstimator, TransformerMixin):

    def __init__(self):
        self.total_bedrooms_median = None

    def fit(self, X, y=None):
        self.total_bedrooms_median = X["total_bedrooms"].median()
        return self


    def transform(self, X):
        X = X.copy()

      #  X.drop(columns=['ocean_proximity'], axis=1, inplace=True)
    
        X["total_bedrooms"] = X["total_bedrooms"].fillna(
            self.total_bedrooms_median
        )


        X["ave_occupancy"] = (
            X["population"] / X["households"]
        )

        X["ave_rooms"] = (
            X["total_rooms"] / X["households"]
        )


        X['rooms_per_household'] = (	 
            X['total_rooms'] /  X["households"] 
         )


        X["bedrooms_per_room"] = ( 
 	         X["total_bedrooms"] / X["total_rooms"]
        )

        X.drop(["total_rooms","ave_occupancy","households","housing_median_age"],axis=1,inplace=True)


        return X