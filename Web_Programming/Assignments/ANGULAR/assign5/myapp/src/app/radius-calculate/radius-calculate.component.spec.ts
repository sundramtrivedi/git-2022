import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RadiusCalculateComponent } from './radius-calculate.component';

describe('RadiusCalculateComponent', () => {
  let component: RadiusCalculateComponent;
  let fixture: ComponentFixture<RadiusCalculateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RadiusCalculateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RadiusCalculateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
