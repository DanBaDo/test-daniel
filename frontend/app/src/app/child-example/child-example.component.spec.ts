import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChildExampleComponent } from './child-example.component';

describe('ChildExampleComponent', () => {
  let component: ChildExampleComponent;
  let fixture: ComponentFixture<ChildExampleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChildExampleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChildExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
