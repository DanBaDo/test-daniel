import { Component, OnInit } from '@angular/core';

import { ContextService } from '../services/context.service';

@Component({
  selector: 'app-child-example',
  templateUrl: './child-example.component.html',
  styleUrls: ['./child-example.component.css']
})
export class ChildExampleComponent implements OnInit {

  constructor(
    public context: ContextService
  ) { }

  ngOnInit(): void {
    console.log(this.context.data.counter++);
  }

}
