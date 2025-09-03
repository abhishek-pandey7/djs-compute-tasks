# djs-compute-tasks
## UFC Fighters Data Analysis

This project performs EDA on UFC fighters’ statistics to learn about about performance, fighting styles, and key factors that contribute to success.

### Visualizations and Insights

#### 1.Correlation Heatmap
- It shows that **wins** strongly correlate with **total fights**, and **losses** also strongly correlate with **total fights**, as expected.
- **Height** and **reach** have a strong positive correlation. 
- The **win percentage** is positively correlated with **striking accuracy** and **strikes landed per minute**. This shows that fighters who are more accurate with their strikes and land more strikes per minute, have a higher chance of winning.
- **Age** has negative correlation with **win percentage**. This may be because as a person grows older, his performance also tends to decline. Hence a younger person may have a higher win percentage.

#### 2. Distribution of wins
- Most fighters have **fewer than 30 wins**.  
- A small number of fighters have significantly higher wins.  

#### 3. Average wins by stance
- **Southpaw** and **Open stance** fighters have slightly higher average wins. 
- **Sideways stance** is rare and less successful.

#### 4. Height vs reach
- Taller fighters have longer reach and the relationship between them is linear.

#### 5. Strikes landed vs Strikes absorbed (Highlighted by win%)
- Fighters with **higher strikes landed per minute** and **lower strikes absorbed** generally show higher win percentages.  
- Fighters with more strikes with less absorbed are successful 

#### 6. Distribution of fighter stances
- **Orthodox stance** dominates, followed by **Southpaw**.  
- Other stances like **Switch, Sideways, and Open** are rare.  

#### 7. Win Percentage by Stance
- **Switch stance** show the highest win percentage.  
- **Sideways** has lowest win percentage

#### 8. Age vs Win Percentage
- Peak performance occurs in the **late 20s to early 30s**.
- Win percentage **declines with age**, especially after 40. 

#### 9. Distribution of average takedowns landed per 15 mins
- Most fighters attempt **very few takedowns per 15 minutes**.  

#### 10. Height vs Win Percentage
- Height **does not have a strong influence** on win percentage. 

#### 11. Win perecentage vs Significant striking accuracy
- As striking accuracy increases from about 10% to 80%, win percentage generally rises from nearly 50% to 75-80%.
- After around 80% accuracy, win percentage actually starts to decline slightly, which could suggest:
    a- Small sample size at this level.
    b- less strikes but high accuracy

#### 12. Strike defense vs Strikes absorbed
- Fighters with higher strike defense absorb fewer strikes per minute.

#### 13. Age groups vs win percentage
- Win percentage **decreases with age**.
- Fighters aged between 20 and 25 have highest win percentage and it gets lower as age group increases. 
- We can infer that age group negatively affects performance, probably due to physical decline and slower reflexes.

### Conclusion
1. **Skills like striking accuracy, defense, takedowns** matter more than physical traits like height,weight and reach alone.  
2. **Younger fighters** tend to perform better, peaking before their mid-30s.  
3. **Fighting stance** influences success: Switch, Southpaw, and Orthodox are most effective.  
4. A **balance of strikes landed** and **strikes absorbed** drives higher win percentages.  
5. There are some outliers, which go against the trends. Like older figthers with higher win rates or low defense strikers that absorb more strikes. 
6. Defense matters because fighters with better defense tend to absorb lesser strikes. 
