import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';
import { User } from '../models/Users';
import { ContextService } from '../services/context.service';

@Component({
  selector: 'app-parent-example',
  templateUrl: './parent-example.component.html',
  styleUrls: ['./parent-example.component.css']
})
export class ParentExampleComponent implements OnInit {

  users: User[] = []

  constructor(
    private api: ApiService,
    public context: ContextService
  ) { }

  async ngOnInit(): Promise<void> {
    this.users = await this.api.getUsers()
  }

}
