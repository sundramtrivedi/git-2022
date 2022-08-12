import { Component, OnInit } from '@angular/core';
import { Student } from './student';

@Component({
  selector: 'app-student',
  templateUrl: './student.component.html',
  styleUrls: ['./student.component.css']
})
export class StudentComponent  {

  constructor(name: string, rollNo : number, mark1 : number, mark2 : number, mark3 : number) 
  { 
    Students =  [
                    new Student('John', 2, 55, 79, 85 ),
                    new Student('Peter', 5, 35, 50, 65 ),
                    new Student('Brij', 7, 85, 90, 92 )
                ];
  }
  
}
