function zero_ending(...arr)
{
	let scores = []
	for(var i = 0 ; i < arr.length ; i++)
	{
		if(arr[i] % 10 == 0)
		{
			scores.push(arr[i])
		}
	}
	return scores
}
console.log(zero_ending(10,30,22,44,60,77,80))