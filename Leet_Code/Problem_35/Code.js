/**
 * Definition for Employee.
 * function Employee(id, importance, subordinates) {
 *     this.id = id;
 *     this.importance = importance;
 *     this.subordinates = subordinates;
 * }
 */

/**
 * @param {Employee[]} employees
 * @param {number} id
 * @return {number}
 */
 var GetImportance = function(employees, id) {
    var sum_importance = 0;
    
    for(let k = 0; k < employees.length; k++)
    {
        if(employees[k][0] === id)
        {
            sum_importance += employees[k][1]; 
            for(let i = 0; i < employees[k][2].length; i++)
            {
                for(let j = 0; j < employees.length; j++)
                {
                    if(employees[j][0] === id)
                    {
                        continue;
                    }
                    else
                    {
                        if(employees[k][2][i] === employees[j][0])
                        {
                            sum_importance += employees[j][1];
                        }

                    }
                }
            }
            break;
        }
        else 
        {
            continue;
        }
    }
    
    return sum_importance;
        
};
var GetImportance1 = function(employees, id) {
    const map = new Map(employees.map(({id, importance, subordinates }) => [id, {importance, subordinates}]));  
    const count = (e) => e.importance + e.subordinates.reduce((a,c) => a + count(map.get(c)), 0)
    return count(map.get(id));
};