var start = prompt("Type y to start, n to close");
names_array = []
if (start === 'y'){
    do{
        var choice = prompt("Enter your choice: add, remove, display, quit");
        if(choice === "add"){
            var name = prompt("Enter name to be added:");
            names_array.push(name);
        }
        else if(choice === "remove"){
            var name = prompt("Enter name to be added:");
            var i = 0;
            for( ; i < names_array.length; i++)
                if(names_array[i] === name)
                    break;

            for(var j = i + 1; j < names_array.length; j++)
                names_array[j - 1] = names_array[j];
            names_array.pop();

            //OR
            // var i = names_array.indexOf(name);
            // names_array.splice(i, 1);
        }
        else if(choice === "display"){
            console.log(names_array);
        }
    }while(choice !== "quit");
}
