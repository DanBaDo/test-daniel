import { Injectable } from '@angular/core';

import { ConfigService } from './config.service';
import { User } from '../models/Users';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  async getUsers () {
    let users: User[]
    const response = await fetch(this.config.BACKEND + '/users/')
    const data = await response.json()
    return data.results
  }

  constructor(
    private config: ConfigService
  ) {}
}
