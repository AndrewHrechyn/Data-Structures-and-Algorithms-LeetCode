class StockPrice {
public:

    map<int, int> field, frequency;
    int maxTimeStamp = -1;
    StockPrice() {
        
    }
    
    void update(int timestamp, int price) {
        if(field.find(timestamp) != field.end()){
            int prev = field[timestamp];
            frequency[prev]--;
            if(frequency[prev] == 0){
                frequency.erase(prev);
            }
        }
        field[timestamp] = price;
        frequency[price]++;
        if(timestamp > maxTimeStamp){
            maxTimeStamp = timestamp;
        }

    }
    
    int current() {
        return field[maxTimeStamp];
    }
    
    int maximum() {
        int maximum_price = 0;
        maximum_price = frequency.rbegin() -> first;
        return maximum_price;
    }
    
    int minimum() {
        int minimum_price = 0;
        minimum_price = frequency.begin() -> first;
        return minimum_price;
    }
};