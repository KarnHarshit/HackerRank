def find_runner_up_score(scores):
    # Remove duplicates and sort the scores in descending order
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    
    # The runner-up score will be the second highest score in the sorted list
    runner_up_score = unique_scores[1]
    
    return runner_up_score

# Example usage
if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    runner_up_score = find_runner_up_score(scores)
    print(runner_up_score)
