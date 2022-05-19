import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { ConfigService } from './config.service';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    private config: ConfigService,
    private request: HttpClient
  ) {}

  getInspections () {
    return this.request.get(this.config.BACKEND + '/api/solargrade/inpsections',{responseType:'json'})
  }
}
