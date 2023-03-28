# Survey Questions

## SEXVAR

What is your sex?

- Male
- Female

```
0-female
1-male
```

## GENHLTH

Would you say that in general your health is:
- Excellent
- Very good
- Good
- Fair
- Poor

```
0-Excellent
1-Very good
2-Good
3-Fair
4-Poor
```

## PHYSHLTH

Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? 

```
Enter number of days: 0-30
```

## MENTHLTH

Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?

```
Enter number of days: 0-30
```

## POORHLTH
During the past 30 days, for about how many days did poor physical or mental health keep you from doing your usual activities, such as self-care, work, or recreation?

```
Enter number of days 0-30
```

## PERSDOC3

Do you have one person (or a group of doctors) that you think of as your personal health care provider?

```
0-no doctor
1-a personal doctor (or more than 1)
```

## MEDCOST1

Was there a time in the past 12 months when you needed to see a doctor but could not because you could not afford it?

```
0-No
1-Yes
```

## CHECKUP1

Have you visited a doctor for a routine checkup within the past year (< 12 months ago)? [A routine checkup is a general physical exam, not an exam for a specific injury, illness, or condition.]

```
0-No
1-Yes
```

## EXERANY2

During the past month, other than your regular job, did you participate in any physical activities or exercises such as running, calisthenics, golf, gardening, or walking for exercise?

```
0-No
1-Yes
```

## BPHIGH6

Have you ever been told by a doctor, nurse or other health professional that you have high blood pressure? (If  ́Yes ́ and respondent is female, ask  ́Was this only when you were pregnant? ́.)

### high_blood_pressure

```
0-Yes, but only during pregnancy
0-No
0-Told borderline high or pre-hypertensive or elevated blood pressure
1-Yes
```

### pregnant_high_blood_pressure

```
1-Yes, but only during pregnancy
0-No
0-Told borderline high or pre-hypertensive or elevated blood pressure
0-Yes
```

### borderline_high_blood_pressure

```
0-Yes, but only during pregnancy
0-No
1-Told borderline high or pre-hypertensive or elevated blood pressure
0-Yes
```

## BPMEDS

Are you currently taking medicine for your high blood pressure?

```
0-No
1-Yes
```

## CHOLCHK3 (cholesterol_checked_within_year)

Have you had your cholesterol checked within the past year (anytime < one year ago)?

```
0-No
1-Yes
```

## TOLDHI3

Have you ever been told by a doctor, nurse or other health professional that your cholesterol is high?

```
0-No
1-Yes
```

## CHOLMED3

Are you currently taking medicine prescribed by your doctor or other health professional for your cholesterol?

```
0-No
1-Yes
```

## MARITAL

Are you: (marital status)
- Married
- Divorced
- Widowed
- Separated
- Never married
- A member of an unmarried couple


### married

```
1-Married
0-Divorced
0-Widowed
0-Separated
0-Never married
0-A member of an unmarried couple
```

### divorced

```
0-Married
1-Divorced
0-Widowed
0-Separated
0-Never married
0-A member of an unmarried couple
```

### widowed

```
0-Married
0-Divorced
1-Widowed
0-Separated
0-Never married
0-A member of an unmarried couple
```

### separated

```
0-Married
0-Divorced
0-Widowed
1-Separated
0-Never married
0-A member of an unmarried couple
```

### never_married

```
0-Married
0-Divorced
0-Widowed
0-Separated
1-Never married
0-A member of an unmarried couple
```

### unmarried_couple

```
0-Married
0-Divorced
0-Widowed
0-Separated
0-Never married
1-A member of an unmarried couple
```

## RENTHOM1

Do you own or rent your home?

- Own
- Rent
- Other arrangement

### own_house

```
1-Own
0-Rent
0-Other arrangement
```

### renting

```
0-Own
1-Rent
0-Other arrangement
```

### other_arrangement_housing

```
0-Own
0-Rent
1-Other arrangement
```

## VETERAN3

Have you ever served on active duty in the military?

```
0-No
1-Yes
```

## EMPLOY1

Are you currently...?

- Employed for wages 
- Self-employed 
- Out of work for 1 year or more
- Out of work for < 1 year
- A homemaker
- A student
- Retire
- Unable to work

### employed_for_wages

```
1-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
0-A student
0-Retire
0-Unable to work
```

### self_employed

```
0-Employed for wages 
1-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
0-A student
0-Retire
0-Unable to work
```

### out_of_work_year_plus

```
0-Employed for wages 
0-Self-employed 
1-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
0-A student
0-Retire
0-Unable to work
```

### out_of_work_year_less

```
0-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
1-Out of work for < 1 year
0-A homemaker
0-A student
0-Retire
0-Unable to work
```

### homemaker

```
0-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
1-A homemaker
0-A student
0-Retire
0-Unable to work
```

### student

```
0-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
1-A student
0-Retire
0-Unable to work
```

### retired

```
0-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
0-A student
1-Retire
0-Unable to work
```

### unable_to_work

```
0-Employed for wages 
0-Self-employed 
0-Out of work for 1 year or more
0-Out of work for < 1 year
0-A homemaker
0-A student
0-Retire
1-Unable to work
```

## PREGNANT

To your knowledge, are you now pregnant?

```
0-No
1-Yes
```

## DEAF

Are you deaf or do you have serious difficulty hearing?

```
0-No
1-Yes
```

## BLIND

Are you blind or do you have serious difficulty seeing, even when wearing glasses?

```
0-No
1-Yes
```

## DECIDE

Because of a physical, mental, or emotional condition, do you have serious difficulty concentrating, remembering, or making decisions?

```
0-No
1-Yes
```

## DIFFWALK

Do you have serious difficulty walking or climbing stairs?

```
0-No
1-Yes
```

## DIFFDRES

Do you have difficulty dressing or bathing?

```
0-No
1-Yes
```

## DIFFALON

Because of a physical, mental, or emotional condition, do you have difficulty doing errands alone such as visiting a doctor ́s office or shopping?

```
0-No
1-Yes
```

## SMOKE100

Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]

```
0-No
1-Yes
```

## SMOKDAY2

Do you now smoke cigarettes every day, some days, or not at all?

- Every day
- Some days
- Not at all

### smoke_every_day

```
1-Every day
0-Some days
0-Not at all
```

### smoke_some_days

```
0-Every day
1-Some days
0-Not at all
```

### smoke_not_at_all

```
0-Every day
0-Some days
1-Not at all
```

## USENOW3

Do you currently use chewing tobacco, snuff, or snus every day, some days, or not at all? (Snus (Swedish for snuff) is a moist smokeless tobacco, usually sold in small pouches that are placed under the lip against the gum.)

- Every day
- Some days
- Not at all


### smokeless_every_day

```
1-Every day
0-Some days
0-Not at all
```

### smokeless_some_days

```
0-Every day
1-Some days
0-Not at all
```

### smokeless_not_at_all

```
0-Every day
0-Some days
1-Not at all
```

## ECIGNOW1

Do you now use e-cigarettes or other electronic vaping products every day, some days, or not at all?

- Every day
- Some days
- Not at all
- Never used e-cigs


### ecig_every_day

```
1-Every day
0-Some days
0-Not at all
0-Never used e-cigs
```

### ecig_some_days

```
0-Every day
1-Some days
0-Not at all
0-Never used e-cigs
```

### ecig_not_at_all

```
0-Every day
0-Some days
1-Not at all
0-Never used e-cigs
```

### ecig_never_used

```
0-Every day
0-Some days
0-Not at all
1-Never used e-cigs
```

## ALCDAY5

During the past 30 days, how many days per month did you have at least one drink of any alcoholic beverage such as beer, wine, a malt beverage or liquor?

```
0-30 number of days
```

## AVEDRNK3

One drink is equivalent to a 12-ounce beer, a 5-ounce glass of wine, or a drink with one shot of liquor. During the past 30 days, on the days when you drank, about how many drinks did you drink on the average? (A 40 ounce beer would count as 3 drinks, or a cocktail drink with 2 shots would count as 2 drinks.)

```
0-76 number of drinks
```

## DRNK3GE5

Considering all types of alcoholic beverages, how many times during the past 30 days did you have 5 or more drinks for men or 4 or more drinks for women on an occasion?

```
0-76 number of times
```

## MAXDRNKS

During the past 30 days, what is the largest number of drinks you had on any occasion?

```
0-76
```

## FLUSHOT7

During the past 12 months, have you had either flu vaccine that was sprayed in your nose or flu shot injected into your arm?

```
0-No
1-Yes
```

## PNEUVAC4

Have you ever had a pneumonia shot also known as a pneumococcal vaccine?

```
0-No
1-Yes
```

## HIVTST7

Including fluid testing from your mouth, but not including tests you may have had for blood donation, have you ever been tested for H.I.V?

```
0-No
1-Yes
```

## _METSTAT

Do you live in a metropolitan area?

```
0-No
1-Yes
```

## _URBSTAT

Do you live in an...?

- Urban county
- Rural county

```
0-Rural county
1-Urban county
```

## _IMPRACE

What do you consider to be your race/ethnicity?

- White, Non-Hispanic
- Black, Non-Hispanic
- Asian, Non-Hispanic
- American Indian/Alaskan Native, Non-Hispanic 
- Hispanic 
- Other race, Non-Hispanic

### white

```
1-White, Non-Hispanic
0-Black, Non-Hispanic
0-Asian, Non-Hispanic
0-American Indian/Alaskan Native, Non-Hispanic 
0-Hispanic 
0-Other race, Non-Hispanic
```

### black

```
0-White, Non-Hispanic
1-Black, Non-Hispanic
0-Asian, Non-Hispanic
0-American Indian/Alaskan Native, Non-Hispanic 
0-Hispanic 
0-Other race, Non-Hispanic
```

### asian

```
0-White, Non-Hispanic
0-Black, Non-Hispanic
1-Asian, Non-Hispanic
0-American Indian/Alaskan Native, Non-Hispanic 
0-Hispanic 
0-Other race, Non-Hispanic
```

### native

```
0-White, Non-Hispanic
0-Black, Non-Hispanic
0-Asian, Non-Hispanic
1-American Indian/Alaskan Native, Non-Hispanic 
0-Hispanic 
0-Other race, Non-Hispanic
```

### hispanic

```
0-White, Non-Hispanic
0-Black, Non-Hispanic
0-Asian, Non-Hispanic
0-American Indian/Alaskan Native, Non-Hispanic 
1-Hispanic 
0-Other race, Non-Hispanic
```

## _HLTHPLN

Do you have some form of health insurance?

```
0-No
1-Yes
```

## _AGE80

How old are you?

```
18-80 (if under 18 assume 18, if over 80 assume 80)
```

## HTIN4

How tall are you in inches?

```
36-95 (if under 36 assume 36, if over 95 assume 95)
```

## WTKG3

How much do you weigh in kilograms?

```
23.00-295.00 (if under 23 assume 23, if over 295 assume 295)
```

## _EDUCAG

What Level of education have you completed?

- Did not graduate High School
- Graduated High School
- Attended College or Technical School
- Graduated from College or Technical School

### not_graduate_high_school

```
1-Did not graduate High School
0-Graduated High School
0-Attended College or Technical School
0-Graduated from College or Technical School
```

### graduated_high_school

```
0-Did not graduate High School
1-Graduated High School
0-Attended College or Technical School
0-Graduated from College or Technical School
```

### attended_college

```
0-Did not graduate High School
0-Graduated High School
1-Attended College or Technical School
0-Graduated from College or Technical School
```

### graduated_college

```
0-Did not graduate High School
0-Graduated High School
0-Attended College or Technical School
1-Graduated from College or Technical School
```

## _INCOMG1

How is your income?

- Less than $15,000
- $15,000 to < $25,000
- $25,000 to < $35,000
- $35,000 to < $50,000
- $50,000 to < $100,000
- $100,000 to < $200,000
- $200,000 or more

```
1-Less than $15,000
2-$15,000 to < $25,000
3-$25,000 to < $35,000
4-$35,000 to < $50,000
5-$50,000 to < $100,000
6-$100,000 to < $200,000
7-$200,000 or more
```

## FTJUDA2_

Not including fruit-flavored drinks or fruit juices with added sugar, how often did you drink 100% fruit juice such as apple or orange juice?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```

## FRUTDA2_

Not including juices, how often did you eat fruit?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```

## GRENDA1_

How often did you eat a green leafy or lettuce salad, with or without other vegetables?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```

## FRNCHDA_

How often did you eat any kind of fried potatoes, including french fries, home fries, or hash browns?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```

## POTADA1_

How often did you eat any other kind of potatoes, or sweet potatoes, such as baked, boiled, mashed potatoes, or potato salad?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```

## VEGEDA2_

Not including lettuce salads and potatoes, how often did you eat other vegetables?

```
- ___number___ times per [drop down selector]
                           |_day
                           |_week
                           |_month
                           |_year 
```

```
value range = 0.00-99.99
[DAY] value = *number* 
[WEEK] value = *number* / 7
[MONTH] value = *number* / 30
[year] value = *number* / 365

if value over 99.99 assume 99.99
```


