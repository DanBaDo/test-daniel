import { Component, OnInit } from '@angular/core';

import { ApiService } from '../services/api.service';
import { ContextService } from '../services/context.service';
import { Inspection } from '../services/models';

@Component({
  selector: 'app-parent-example',
  templateUrl: './parent-example.component.html',
  styleUrls: ['./parent-example.component.css']
})
export class ParentExampleComponent {

  inspections: Inspection[] = []
  totalWarnings: number = 0
  totalCriticals: number = 0

  constructor(
    private api: ApiService,
    public context: ContextService,
  ) {
    this.api.getInspections()
    .subscribe(
      (data) => {
        let currentWarnings = 0
        let currentCriticals = 0
        data.results.forEach( item => {
          currentWarnings += item.issuesWarningCount
          currentCriticals += item.issuesCriticalCount
        });
        this.inspections = data.results
        this.totalWarnings = currentWarnings
        this.totalCriticals = currentCriticals
        console.log(data)
      }
    )
  }
}
