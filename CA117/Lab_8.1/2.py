from gaa_comp_081 import Score

def main():

    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 12)


    assert(s2 == s3)


if __name__ == '__main__':
    main()
