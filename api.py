import requests

access_token = "v^1.1#i^1#p^1#r^0#f^0#I^3#t^H4sIAAAAAAAAAOVYf2wTVRxf121kQQYJRgmaUA8NCOn1rtcf18ta047NNdnWaguOETPvx7vu7PWuufeOronitggmEiImCAH/cMZE0USJIYAooH84Ywyo/DDiJAb/QN1iQkDDD3Ho662MbpIxthqXeP9c3nvfn5/3/fHeo3pqaldsat50eZ5tTmV/D9VTabPRc6namuqVdfbKxdUVVAmBrb/nwZ6qPvsv9ZDPqFnucQCzugaBozujapCzJoOEaWiczkMFchqfAZBDIpcIt7ZwbpLisoaOdFFXCUd0VZDwUiwrCn6KEnjRH/D58ax2Q2ZSDxJ8gPa6GYn2s34JiKKI1yE0QVSDiNdQkHBTbtpJsU43k6QYzuvhaJr0+N0dhGMNMKCia5iEpIiQZS5n8Roltk5uKg8hMBAWQoSi4aZELBxd1diWrHeVyAoVcUggHplw/KhBl4BjDa+aYHI10KLmEqYoAggJV2hUw3ihXPiGMdMw34KaEQRZDACZEXgfg2EvC5RNupHh0eR2FGYUySlbpBzQkILyt0MUoyE8DURUHLVhEdFVjsLvMZNXFVkBRpBojITXhuNxItSitPLOlK5LMK1ozkSk3cmyHh8j0jTlpAOC1yfITFHJqKQixBO0NOiapBQAg442HUUAthhMxMVTggsmimkxIyyjgjWldN4b+PnYjsKGju6gibq0wp6CDAbBYQ1vj/4YN0KGIpgIjEmYuGDBg1Mmm1UkYuKiFYfF0OmGQaILoSzncuVyOTLHkLqRcrkpina1t7YkxC6Q4YkibSHXu6FyewanYrkiAswJFQ7ls9iWbhyn2AAtRYQYH+ujPUXcx5sVmjj7j4kSn13js6Fc2eGVRUb2+90sS4kexi+XIztCxQB1FewAAp93ZngjDVBW5UXgFHGcmRlgKBLHeGU3w8rAKfkCstMTkGWn4JV8TloGgAJAEMQA+39JkqmGeQKIBkBli/OyxHgKBlBLS649RicelZpS7V1NwMfQLatT0Ug80hyPt7an9FiCoY2OVHCqmXBL5xtUBSOTxPrLCUAh12cOQrMOEZBm5F5C1LMgrquKmJ9dG8wYUpw3UD5i5vE4AVQV/2bkajibjZavWpfFyTsoFNPzubwd6j/oTrf0ChaCdnZ5VeCHWACfVchC/yFFPePSeXzwcBVyHU93WlY7JiEcI3IJZp5MmQAibImEz35TZlJwISdxK5OmzjLaKLETU2fBFwvJFNG0FFkdmcRoKqkuBO9IZ/dMQBFMNT2joFPwhWFWhRx2d9RvRRo96ZOW8yRcL5IGgLpp4EsOGSscfpN6Gmj4OIEMXVWBsYaecSHNZEzECyqYbRW1DNVF4ad/1qnqs334r/hF+9wBX4BivTPbOtE6zXTOtp5Qzj54B/cZ1/iXlVCF9dF9tsNUn+1gpc1G+bH+ldTDNfbVVfa7CIgrCQl5TRL0blLhZRIXMY1HpgHINMhnecWorLEpg6fEKyVvOv1PUovGXnVq7fTckice6v6bK9X0/HvnuWmKdTMU4/XQdAe19OZqFX1P1d0jI7Fr3z5/7dJGCr67aejqtfRPO9upeWNENlt1BQ7AitDCU4sb6xctQj9+sr1+R2PrUCfYs8MWe2+g98o3nV+v+zjY9Grjxexv6+JvHx/c8ObmFw+tdTS3adGFHSePnzIHz/XSH4ycPP/cCXrvhe8+7b7uX3Y6vzNXf2DgFXVv/uhnw3ueOfPF1ZP08d2fP1AXXBBYuZlJb1F+9e5YPnxwDju/4ec/127dMiCc27Dd29u/8w2l8mIwqF+w7956MbLr0vIlf+yve+jlv06kz+/7yrcic3n/3NeenfPIoUT7iGtZ7IdtMebMkcsftUT7Go7UDfcNDCc7Wr9/4cCWl5h9Z/ml608/seSSffBoz/WNsS/fYpa9s9F97PXDQ+drn1qweNt9bcn3h4793nv0bC4zuo1/A8Bjgj5tEwAA"

my_headers = {'Authorization' : 'Bearer v^1.1#i^1#p^1#r^0#f^0#I^3#t^H4sIAAAAAAAAAOVYf2wTVRxf121kQQYJRgmaUA8NCOn1rtcf18ta047NNdnWaguOETPvx7vu7PWuufeOronitggmEiImCAH/cMZE0USJIYAooH84Ywyo/DDiJAb/QN1iQkDDD3Ho662MbpIxthqXeP9c3nvfn5/3/fHeo3pqaldsat50eZ5tTmV/D9VTabPRc6namuqVdfbKxdUVVAmBrb/nwZ6qPvsv9ZDPqFnucQCzugaBozujapCzJoOEaWiczkMFchqfAZBDIpcIt7ZwbpLisoaOdFFXCUd0VZDwUiwrCn6KEnjRH/D58ax2Q2ZSDxJ8gPa6GYn2s34JiKKI1yE0QVSDiNdQkHBTbtpJsU43k6QYzuvhaJr0+N0dhGMNMKCia5iEpIiQZS5n8Roltk5uKg8hMBAWQoSi4aZELBxd1diWrHeVyAoVcUggHplw/KhBl4BjDa+aYHI10KLmEqYoAggJV2hUw3ihXPiGMdMw34KaEQRZDACZEXgfg2EvC5RNupHh0eR2FGYUySlbpBzQkILyt0MUoyE8DURUHLVhEdFVjsLvMZNXFVkBRpBojITXhuNxItSitPLOlK5LMK1ozkSk3cmyHh8j0jTlpAOC1yfITFHJqKQixBO0NOiapBQAg442HUUAthhMxMVTggsmimkxIyyjgjWldN4b+PnYjsKGju6gibq0wp6CDAbBYQ1vj/4YN0KGIpgIjEmYuGDBg1Mmm1UkYuKiFYfF0OmGQaILoSzncuVyOTLHkLqRcrkpina1t7YkxC6Q4YkibSHXu6FyewanYrkiAswJFQ7ls9iWbhyn2AAtRYQYH+ujPUXcx5sVmjj7j4kSn13js6Fc2eGVRUb2+90sS4kexi+XIztCxQB1FewAAp93ZngjDVBW5UXgFHGcmRlgKBLHeGU3w8rAKfkCstMTkGWn4JV8TloGgAJAEMQA+39JkqmGeQKIBkBli/OyxHgKBlBLS649RicelZpS7V1NwMfQLatT0Ug80hyPt7an9FiCoY2OVHCqmXBL5xtUBSOTxPrLCUAh12cOQrMOEZBm5F5C1LMgrquKmJ9dG8wYUpw3UD5i5vE4AVQV/2bkajibjZavWpfFyTsoFNPzubwd6j/oTrf0ChaCdnZ5VeCHWACfVchC/yFFPePSeXzwcBVyHU93WlY7JiEcI3IJZp5MmQAibImEz35TZlJwISdxK5OmzjLaKLETU2fBFwvJFNG0FFkdmcRoKqkuBO9IZ/dMQBFMNT2joFPwhWFWhRx2d9RvRRo96ZOW8yRcL5IGgLpp4EsOGSscfpN6Gmj4OIEMXVWBsYaecSHNZEzECyqYbRW1DNVF4ad/1qnqs334r/hF+9wBX4BivTPbOtE6zXTOtp5Qzj54B/cZ1/iXlVCF9dF9tsNUn+1gpc1G+bH+ldTDNfbVVfa7CIgrCQl5TRL0blLhZRIXMY1HpgHINMhnecWorLEpg6fEKyVvOv1PUovGXnVq7fTckice6v6bK9X0/HvnuWmKdTMU4/XQdAe19OZqFX1P1d0jI7Fr3z5/7dJGCr67aejqtfRPO9upeWNENlt1BQ7AitDCU4sb6xctQj9+sr1+R2PrUCfYs8MWe2+g98o3nV+v+zjY9Grjxexv6+JvHx/c8ObmFw+tdTS3adGFHSePnzIHz/XSH4ycPP/cCXrvhe8+7b7uX3Y6vzNXf2DgFXVv/uhnw3ueOfPF1ZP08d2fP1AXXBBYuZlJb1F+9e5YPnxwDju/4ec/127dMiCc27Dd29u/8w2l8mIwqF+w7956MbLr0vIlf+yve+jlv06kz+/7yrcic3n/3NeenfPIoUT7iGtZ7IdtMebMkcsftUT7Go7UDfcNDCc7Wr9/4cCWl5h9Z/ml608/seSSffBoz/WNsS/fYpa9s9F97PXDQ+drn1qweNt9bcn3h4793nv0bC4zuo1/A8Bjgj5tEwAA'}
response = requests.get("https://api.sandbox.ebay.com/buy/browse/v1/item_summary/methods/search?q=facewash", headers=my_headers)
print(response.json())