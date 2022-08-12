import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RadiusCalculateComponent } from './radius-calculate/radius-calculate.component';
import { TodoListComponent } from './todo-list/todo-list.component';
import { StudComponent } from './stud/stud.component';
import { StudentComponent } from './student/student.component';

@NgModule({
  declarations: [
    AppComponent,
    RadiusCalculateComponent,
    TodoListComponent,
    StudComponent,
    StudentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
