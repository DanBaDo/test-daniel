import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { ContextService } from '../services/context.service';
import { take } from 'rxjs';

@Component({
  selector: 'app-parent-example',
  templateUrl: './parent-example.component.html',
  styleUrls: ['./parent-example.component.css']
})
export class ParentExampleComponent implements OnInit {

  inspections: any = {}

  constructor(
    private api: ApiService,
    public context: ContextService,
  ) {
    this.api.getInspections()
    .subscribe(
      (data) => {
        this.inspections = data.results
        console.log(data);
      }
    )
  }

  async ngOnInit() {}

}
