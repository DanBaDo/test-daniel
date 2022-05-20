import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { ConfigService } from './config.service';
import { ApiResponse, Inspection } from './models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(
    private config: ConfigService,
    private request: HttpClient
  ) {}

  getInspections () {
    return this.request.get<ApiResponse<Inspection>>(this.config.BACKEND + '/api/solargrade/inpsections',{responseType:'json'})
  }
}
