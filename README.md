## ERPNext Extensions on Request for Quotation and Supplier Quotation to include Committee Bid Openings

**Committee**
The system allows setting up of quote/bid opening committee, and the committee members that will open quotes or bids once their opening date and time is due.

**Setting Closing Date, and quote opening committee on Request for Quotation**
![image](https://github.com/navariltd/navari_rfq_opening/assets/1822868/9ee5ac7b-fa73-4fb2-be17-97930154bfe8)


**Supplier Quotations Opening**
At the time RFQs are being sent to suppliers, a ToDo record is created for each committee member, who will access it on the opening date and time, and open the quotes submitted against the RFQ. Supplier quotations are only accessible, after they have been opened by all the comittee members set for the RFQ.

### Installation

Using bench, [install ERPNext](https://github.com/frappe/bench#installation) as mentioned here.

Once ERPNext is installed, add rfq_opening_process app to your bench by running

```sh
$ bench get-app https://github.com/navariltd/rfq_opening_process.git
```

After that, you can install rfq_opening_process app on required site by running

```sh
$ bench --site [site.name] install-app rfq_opening_process
```
#### License

GNU General Public License (v3)
