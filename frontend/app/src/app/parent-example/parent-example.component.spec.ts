import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ParentExampleComponent } from './parent-example.component';

describe('ParentExampleComponent', () => {
  let component: ParentExampleComponent;
  let fixture: ComponentFixture<ParentExampleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ParentExampleComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ParentExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
