import pandas as pd
# Filling lowest common SUBSTRING bottom up matrix for first example:
#       s1 = ababbacdee & s2 = haababadeedc (GO BACK AND SEE)
#       | ''|  a | b  |  a |  b | b  | a  |  c |  d | e  | e  |
#   |'' | 0 | 0  |  0 |  0 | 0  | 0  | 0  |  0 | 0  | 0  | 0  |
#   |  h|  0|  0 |  0 | 0  | 0  | 0  | 0  |  0 |  0 |  0 |  0 |
#   | a | 0 |   1|  0 |  1 |  0 |  0 |  1 |  0 |  0 |  0 |  0 |
#   |  a| 0 |  1 |  0 |  1 |  0 |0   | 1  | 0  | 0  | 0  | 0  |
#   |  b| 0 |  0 | 2  |  0 |  2 |  1 |  0 | 0  | 0  | 0  | 0  |
#   |  a| 0 |  1 |  0 |  3 | 0  | 0  |  2 | 0  | 0  |0   |0   |
#   | b | 0 |  0 |  2 |  0 | 4  |  1 |  0 | 0  |0   | 0  |0   |
#   | a | 0 |  1 |  0 | 3  |  0 | 0  |  2 | 0  | 0  | 0  | 0  |
#   |  d| 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |0   |
#   | e | 0 |  0 | 0  | 0  | 0  |  0 | 0  | 0  | 0  | 2  | 1  |
#   |  e| 0 | 0  |  0 |  0 | 0  | 0  | 0  |  0 | 0  |  1 |  3 | 
#   |  d| 0 |  0 |  0 | 0  |  0 |  0 | 0  |  0 |  1 | 0  |  0 |
#   |  c| 0 |  0 |  0 |  0 |  0 |  0 |  0 | 1  |  0 |  0 |  0 |
#
#   Max we can see length is 4, backtracking from here gives us abab, 
#   all other substrings can be found from this matrix where the value is non 0
#

def dp_common_substring(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    dp = [[0] * (s2_len + 1) for _ in range(s1_len + 1)] # one more because of empty string initialisation
                                                         # everything initialised to 0

    substrings = []

    for i in range(1, s1_len + 1):                      # from row 1 to 12th s2
        for j in range(1, s2_len + 1):                  # from col 1 to 10th s1
            if s1[i - 1] == s2[j - 1]:                  # string indexes from 0, but dp indexes from 1 because of initialisation
                dp[i][j] = 1 + dp[i-1][j-1]             # crux, else is always 0
                substrings.append(s1[i - dp[i][j]:i])

    
    return substrings

def main():
    data = {
        'ID': [1, 2, 3, 4, 5, 6],
        'String_1': [
            'ababbacdee',
            'Thisisadocumentcontainingpatienthistory',
            'abcdefgxyz123',
            'The adventurous cat explored the mysterious cave.',
            'Sunflowers bloomed in the radiant sunlight.',
            'Gentle waves lapped against the sandy shore.'
        ],
        'String_2': [
            'haababadeedc',
            'Theletteringinthisstoryisquiteunique',
            'xyz789abcdef',
            'A curious cat ventured into the dark cave for exploration.',
            'Radiant sunlight illuminated the field of blooming sunflowers.',
            'The shore echoed with the soothing sounds of lapping waves.'
        ]
    }

    df = pd.DataFrame(data)

    #string all substrings for all strings here (intermediate)
    substring_rows = []

    for idx, row in df.iterrows():
        s1 = row['String_1']
        s2 = row['String_2']
        id = row['ID']

        #get all common substrings for s1 and s2
        substrings = dp_common_substring(s1, s2)

        #store each one of them
        for sub in substrings:
            substring_rows.append({'ID': id, 'Substring': sub})
    
    #convert all substrings to dataframe
    all_substrings = pd.DataFrame(substring_rows)
    print("Intermediate table containing all common substrings:")
    print(all_substrings)
    print("----------------------------------------------------")
    
    longest_substrings = all_substrings.groupby('ID')['Substring'].apply(lambda x: max(x, key=len)).reset_index()
    longest_substrings.columns = ['ID', 'Longest_common_substring']

    print("Longest common substring (final table):")
    print(longest_substrings)



if __name__ == "__main__":
    main()

    




            

            
