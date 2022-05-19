import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ContextService {

  data = {
    counter: 0
  };

  constructor() { }
}
