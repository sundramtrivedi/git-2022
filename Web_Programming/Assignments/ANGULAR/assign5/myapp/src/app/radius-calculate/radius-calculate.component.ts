import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-radius-calculate',
  templateUrl: './radius-calculate.component.html',
  styleUrls: ['./radius-calculate.component.css']
})
export class RadiusCalculateComponent {
  rad:string=""
  are:number=0
  cir:number=0
  display(rad:string)
  {
    this.are = (Math.PI*(parseInt(rad)*parseInt(rad)));
    this.cir = 2*(Math.PI*parseInt(rad))
  }
  

}
