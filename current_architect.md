                         React

                           |

              ----------------------------

              REST API              WebSocket

                 |                       |

                 ↓                       ↓


                     FastAPI Backend


        -------------------------------

        |              |              |

    Auth System    Room System   Event System


                     |              |

                RoomManager    EventRouter

                                      |

                                      |

                               Event Handlers

                                      |

                               ConnectionManager

                                      |

                               Active WebSockets

                                      |

                               Connected Players