from project import count_schools, isFree, schools, FreeSchools, school_by_name, school_by_city, school_by_country, school_by_language, school_by_level, print_results


def test_count_schools():
    #checkm if count_schools returns correct type
    assert type(count_schools(schools)) == int


def isFree():
    #check if J.K. Mullen High School returns false
    assert isFree("J.K. Mullen High School") == False
    #check if Lynn Classical High School returns true
    assert isFree("Lynn Classical High School") == True


def test_FreeSchools():
    #check if FreeSchools returns correct type
    assert type(FreeSchools(schools)) == list
    #check if FreeSchools returns correct number of schools
    assert len(FreeSchools(schools)) >= 1


def test_school_by_name():
    #check if school_by_name returns correct type
    assert type(school_by_name(schools, "Lynn Classical High School")) == list
    #check if Lynn Classical High School returns a result
    assert len(school_by_name(schools, "Lynn Classical High School")) >= 1
    #check if Lynn classical high SCHOOL returns a result because casing is wrong
    assert len(school_by_name(schools, "LYNN classical high SCHOOL")) >= 1
    #check if Ludzeludze High School returns [] as it does not exist
    assert len(school_by_name(schools, "Ludzeludze High School")) == 0


def test_school_by_level():
    #check if school_by_level returns correct type
    assert type(school_by_level(schools, "High School")) == list
    #check if school_by_level returns correct school
    #check if school_by_level returns [] as Kindergarden does not exist
    assert len(school_by_level(schools, "Kindergarden")) == 0
    #check if HIGH SCHOOL returns a result because casing is wrong
    assert len(school_by_level(schools, "HIGH SCHOOL")) >= 1


def test_school_by_language():
    #check if school_by_language returns correct type
    assert type(school_by_language(schools, "Python")) == list
    #check if school_by_language returns [] as Lucolo does not exist
    assert len(school_by_language(schools, "Lucolo")) == 0
    #check if PYTHON returns a result because casing is wrong
    assert len(school_by_language(schools, "PYTHON")) >= 1


def test_school_by_country():
    #check if school_by_country returns correct type
    assert type(school_by_country(schools, "United States")) == list
    #check if school_by_country returns correct school
    #check if school_by_country returns [] as Swaziland does not exist
    assert len(school_by_country(schools, "Swaziland")) == 0
    #check if UNITED STATES returns a result because casing is wrong
    assert len(school_by_country(schools, "UNITED STATES")) >= 1


def test_school_by_city():
    #check if school_by_city returns correct type
    assert type(school_by_city(schools, "Lynn")) == list
    #check if school_by_city returns [] as Matsapha does not exist
    assert len(school_by_city(schools, "Matsapha")) == 0
    #check if LYNN returns a result because casing is wrong
    assert len(school_by_city(schools, "LYNN")) >= 1
